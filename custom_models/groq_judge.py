# Read environment variables
import os

# Read .env file
from dotenv import load_dotenv

# Groq SDK
from groq import Groq

# DeepEval base class
from deepeval.models import DeepEvalBaseLLM

# Load .env
load_dotenv()


class GroqJudge(DeepEvalBaseLLM):

    # Constructor
    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    # Required by DeepEval
    def load_model(self):
        return self.client

    # DeepEval calls this method
    def generate(self, prompt: str):

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content

    # Async version required by DeepEval
    async def a_generate(self, prompt: str):
        return self.generate(prompt)

    # Model name shown in reports
    def get_model_name(self):
        return "openai/gpt-oss-20b"