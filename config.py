import os

from dotenv import load_dotenv

# Load .env file if available
load_dotenv()


class Config:
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-2024-08-06")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise OSError("OPENAI_API_KEY is not set in the environment variables.")


Config.validate()
