import json

import google.generativeai as genai

from app.config.settings import (
    settings,
)

class GeminiClient:

    def __init__(self):

        genai.configure(
            api_key=
            settings.GEMINI_API_KEY
        )

        self.model = (
            genai.GenerativeModel(
                "gemini-1.5-pro"
            )
        )
    
        def generate_json(
            self,
            prompt: str,
        ) -> dict:

            response = (
                self.model.generate_content(
                    prompt
                )
            )

            return json.loads(
                response.text
            )