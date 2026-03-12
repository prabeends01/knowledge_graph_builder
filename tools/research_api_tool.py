import os
from euriai import EuriaiClient
from dotenv import load_dotenv

load_dotenv()

_api_key = os.getenv("EURI_API_KEY")
if not _api_key:
    raise RuntimeError("EURI_API_KEY environment variable is missing. Please set it in your .env file or shell.")

EURI_CLIENT = EuriaiClient(
    api_key=_api_key,
    model="gpt-4.1-nano"
)
