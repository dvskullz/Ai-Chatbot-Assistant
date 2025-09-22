def show_skills():
    skills = [
        "Open websites: google, youtube, facebook, linkedin, etc.",
        "Open installed apps: notepad, chrome, calculator, vscode, etc.",
        "Play music from your music library.",
        "Get latest news headlines.",
        "File operations: create, read, append, delete, rename files.",
        "Math calculations: e.g. 'one plus two', '3 * 4', 'ten divided by two'.",
        "Check internet connection.",
        "Run internet speed test.",
        "General conversation and Q&A (powered by Gemini).",
        "Switch between voice and text input modes.",
        "Show system info (RAM usage, input type, etc.)."
    ]
    banner = """
------------------------------------------------------------
                   JARVIS - Skills & Features
------------------------------------------------------------
"""
    print(banner)
    for idx, skill in enumerate(skills, 1):
        print(f"{idx}. {skill}")
    print("------------------------------------------------------------")
    return "I can do things like: " + "; ".join(skills)