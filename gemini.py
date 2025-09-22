# gemini.py
import google.generativeai as genai

class Gemini:
    def __init__(self):
        genai.configure(api_key="AIzaSyDBzpqwFxZeAK1kMVIvGE7x8wj1A0MaXA4")
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate(self, prompt: str):
        return self.model.generate_content(prompt)
