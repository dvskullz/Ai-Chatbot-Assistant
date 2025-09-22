import os
import sys
import winsound
from skills.mymath import calculate
from skills.internet import run_speedtest, internet_availability
from skills.skills import show_skills
from skills.general import clear_console, change_volume, mute_volume, max_volume
from skills.app import open_app
from skills.file import create_file, read_file, append_file, delete_file, rename_file
from skills.activation import  assistant_greeting
from skills.productivity import add_todo, show_todos, set_reminder
from skills.currency import convert_currency
from skills.units import convert_units
from skills.entertainment import tell_joke, tell_quote
import psutil
import pyfiglet
import threading
import time

sys.stderr = open(os.devnull, 'w')
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from gemini import Gemini

recognizer = sr.Recognizer()
engine = pyttsx3.init()
gemini_client = Gemini()

def speak(text):
    if text:
        engine.say(str(text))
        engine.runAndWait()
    else:
        engine.say("Sorry, I did not get a response.")
        engine.runAndWait()

def processCommand(command):
    c = command.lower().strip()
    # --- Exit command ---
    if c in ["close", "exit", "quit", "bye"]:
        speak("Goodbye, take care!")
        print("Goodbye, take care!")
        # disable_assistant()
    # --- File creation by just saying filename and extension ---
    if c.endswith(".txt") or c.endswith(".md") or c.endswith(".docx"):
        filename = c.replace(" ", ".") if " " in c and not "." in c else c
        msg = create_file(filename)
        speak(msg)
        print(msg)
        return
    # --- Standard file commands ---
    if c.startswith("create file"):
        filename = c.replace("create file", "").strip()
        msg = create_file(filename)
        speak(msg)
        print(msg)
        return
    elif c.startswith("read file"):
        filename = c.replace("read file", "").strip()
        content = read_file(filename)
        speak("Reading file.")
        print(content)
        return
    elif c.startswith("append file"):
        parts = c.replace("append file", "").strip().split(" with ")
        if len(parts) == 2:
            filename, content = parts
            msg = append_file(filename.strip(), content.strip())
            speak(msg)
            print(msg)
        else:
            speak("Please specify the file and content to append.")
        return
    elif c.startswith("delete file"):
        filename = c.replace("delete file", "").strip()
        msg = delete_file(filename)
        speak(msg)
        print(msg)
        return
    elif c.startswith("rename file"):
        parts = c.replace("rename file", "").strip().split(" to ")
        if len(parts) == 2:
            old_name, new_name = parts
            msg = rename_file(old_name.strip(), new_name.strip())
            speak(msg)
            print(msg)
        else:
            speak("Please specify the old and new file names.")
        return
    # --- Web commands ---
    site_map = {
        "google": "https://google.com",
        "facebook": "https://facebook.com",
        "youtube": "https://youtube.com",
        "linkedin": "https://linkedin.com"
    }
    opened_any = False
    if "open" in c:
        for site, url in site_map.items():
            if site in c:
                webbrowser.open_new_tab(url)
                speak(f"Opening {site.capitalize()}")
                print(f"Opening {site.capitalize()}")
                opened_any = True
        if opened_any:
            return
    # --- App opening ---
    if c.startswith("open "):
        app_name = c[5:].strip()
        open_app(app_name)
        return
    # --- Greetings ---
    if "hello" in c or "hi" in c:
        speak("Hello! How can I assist you today?")
        print("Greeted the user.")
        return
    # --- Math functionality ---
    if any(op in c for op in ["plus", "minus", "times", "multiplied", "divide", "divided", "+", "-", "*", "/", "%", "mod", "power"]):
        result = calculate(c)
        speak(f"The result is {result}")
        print(f"The result is {result}")
        return
    # --- Internet skills ---
    if any(word in c for word in ["speedtest", "internet speed", "speed"]):
        stop_event = threading.Event()
        spinner_thread = threading.Thread(target=spinner_running, args=(stop_event,))
        spinner_thread.start()
        result = run_speedtest()
        stop_event.set()
        spinner_thread.join()
        speak(result)
        print(result)
        return
    if "internet available" in c or "internet connection" in c or "is internet" in c:
        result = internet_availability()
        speak(result)
        print(result)
        return
    # --- Show skills ---
    if "skills" in c or "what can you do" in c or "help" in c:
        msg = show_skills()
        speak(msg)
        return
    # --- General utility commands ---
    if "clear console" in c:
        msg = clear_console()
        speak(msg)
        print(msg)
        return
    if "increase volume" in c or "raise volume" in c:
        msg = change_volume(10)
        speak(msg)
        print(msg)
        return
    if "decrease volume" in c or "reduce volume" in c or "lower volume" in c:
        msg = change_volume(-10)
        speak(msg)
        print(msg)
        return
    if "mute volume" in c or "mute" in c:
        msg = mute_volume()
        speak(msg)
        print(msg)
        return
    if "max volume" in c or "maximum volume" in c:
        msg = max_volume()
        speak(msg)
        print(msg)
        return
    # --- Productivity ---
    if c.startswith("add task"):
        task = c.replace("add task", "").strip()
        msg = add_todo(task)
        speak(msg)
        print(msg)
        return
    if "show tasks" in c or "show to-do" in c:
        msg = show_todos()
        speak(msg)
        print(msg)
        return
    if c.startswith("remind me to"):
        parts = c.replace("remind me to", "").strip().split(" at ")
        if len(parts) == 2:
            task, time_str = parts
            msg = set_reminder(task.strip(), time_str.strip())
            speak(msg)
            print(msg)
        else:
            speak("Please specify the task and time.")
        return

    # --- Currency ---
    if "convert" in c and any(x in c for x in [" to ", " in "]):
        try:
            parts = c.split()
            amount = float(parts[1])
            from_currency = parts[2]
            # Find "to" or "in" position
            if " to " in c:
                to_idx = parts.index("to")
            else:
                to_idx = parts.index("in")
            to_currency = parts[to_idx + 1]
            msg = convert_currency(amount, from_currency, to_currency)
            speak(msg)
            print(msg)
        except Exception:
            speak("Sorry, I couldn't convert the currency.")
        return

    # --- Unit Conversion ---
    if "convert" in c and any(x in c for x in [" to ", " in "]):
        try:
            parts = c.split()
            amount = float(parts[1])
            from_unit = parts[2]
            if " to " in c:
                to_idx = parts.index("to")
            else:
                to_idx = parts.index("in")
            to_unit = parts[to_idx + 1]
            msg = convert_units(amount, from_unit, to_unit)
            speak(msg)
            print(msg)
        except Exception:
            speak("Sorry, I couldn't convert the units.")
        return

   

    # --- Entertainment ---
    if "joke" in c:
        msg = tell_joke()
        speak(msg)
        print(msg)
        return
    if "quote" in c:
        msg = tell_quote()
        speak(msg)
        print(msg)
        return
    # --- Fallback to Gemini ---
    threaded_gemini_response(c, speak, print, gemini_client)
    return

def show_console_gui(input_type):
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_banner = pyfiglet.figlet_format("JARVIS", font="slant")
    print(ascii_banner)

def play_startup_sound():
    # Play Windows default sound (or use a .wav file path)
    winsound.MessageBeep(winsound.MB_ICONASTERISK)

def spinner_running(event):
    bar = ""
    print("Calculating speed", end='', flush=True)
    while not event.is_set():
        bar += "█"
        print(f"\rCalculating speed {bar}", end='', flush=True)
        time.sleep(0.3)
        if len(bar) > 20:
            bar = ""
    print(" " * 40, end='\r')  # Clear line

def threaded_gemini_response(command, speak, print_func, gemini_client):
    def worker():
        response = gemini_client.generate(command)
        answer = getattr(response, "text", None) or str(response)
        speak(answer)
        print_func(answer)
    t = threading.Thread(target=worker)
    t.start()

if __name__ == "__main__":
    print("Choose input mode: [1] Voice  [2] Text")
    mode = input("Enter 1 for Voice or 2 for Text: ").strip()
    input_type = "Voice" if mode == "1" else "Text" if mode == "2" else "Unknown"
    show_console_gui(input_type)
    greet = assistant_greeting()
    print(greet)
    speak(greet)
    speak("....Initializing Jarvis....")
    # ...rest of your code...
    if mode == "1":
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                while True:
                    print("Listening for your command...")
                    try:
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                        command = recognizer.recognize_google(audio)
                        print(f"Heard: {command}")
                        processCommand(command)
                    except sr.UnknownValueError:
                        print("Could not understand the audio")
                        speak("Could not understand the audio")
                    except sr.WaitTimeoutError:
                        print("Listening timed out, waiting for input...")
                        speak("Listening timed out, waiting for input...")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Could not request results from Google Speech Recognition service.")
        except Exception as e:
            print(f"Error: {e}")
            speak("An error occurred.")
    elif mode == "2":
        while True:
            command = input("Enter your command: ")
            processCommand(command)
    else:
        print("Invalid input mode selected.")
        speak("Invalid input mode selected.")
