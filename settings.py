import os
from dotenv import load_dotenv
load_dotenv()

OPEN_AI_KEY = os.environ.get("OPEN_AI_KEY")
PORT = os.environ.get("PORT")

if not OPEN_AI_KEY:
    raise ValueError("Missing OPEN_AI_KEY key in .env")


settingsConstants = {
    "port": PORT if PORT else "8000",
    "OPEN_AI_KEY": OPEN_AI_KEY,
}
