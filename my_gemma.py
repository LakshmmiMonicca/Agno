import os

import google.generativeai as genai



class Gemma:

    def __init__(self, model_name="gemini-1.5-flash"):

        print("[Gemma __init__] Initializing...")

        api_key = os.getenv("GEMINI_API_KEY")

        print("[Gemma __init__] Loaded API Key:", api_key)

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(model_name)

        self.id = model_name

        self.provider = "gemini"

        #print("[Gemma __init__] Bound response method:", self.response)  # ✅ Debug



    def response(self, prompt, tools=None, messages=None, **kwargs):

        print("[Gemma response] Prompt received:", prompt)

        result = self.model.generate_content(prompt)

        return type("ModelResponse", (object,), {"output": result.text})()



    def get_instructions_for_model(self, tools):

        return "Use these tools wisely."



    def get_system_message_for_model(self, tools):

        return "You are a helpful assistant."

