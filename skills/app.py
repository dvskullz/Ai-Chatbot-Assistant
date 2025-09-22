import os
import subprocess
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Map app names to their executable paths or commands
app_paths = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "paint": "mspaint.exe",
    # Add more apps and their paths as needed
}

def open_app(app_name):
    app_name = app_name.lower()
    path = app_paths.get(app_name)
    if path:
        try:
            # Expand environment variables if present
            path = os.path.expandvars(path)
            subprocess.Popen(path)
            speak(f"Opening {app_name}")
            print(f"Opening {app_name}")
        except Exception as e:
            speak(f"Failed to open {app_name}")
            print(f"Error opening {app_name}: {e}")
    else:
        speak(f"Sorry, I don't know how to open {app_name}")
        print(f"App '{app_name}' not found in app_paths.")

if __name__ == "__main__":
    speak("Which app would you like to open?")
    app = input("Enter app name: ")
    open_app(app)