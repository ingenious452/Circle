import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = DATA_DIR / "logs"
PID_FILE = DATA_DIR / "circled.pid"
STOP_FILE = DATA_DIR / "circled.stop"
DB_FILE = DATA_DIR / "circle.db"

DAEMON_SCRIPT = BASE_DIR / "core" / "daemon" / "daemon.py"

LOG_DIR.mkdir(parents=True, exist_ok=True)

# Telegram
CHAT_ID = os.getenv('CHAT_ID', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')

# Email
EMAIL_USER = os.getenv('EMAIL_USER', '')
TO_EMAIL = os.getenv('TO_EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')
EMAIL_SERVER = os.getenv('EMAIL_SERVER', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 1))

# Mongo DB
MONGO_USER = os.getenv('MONGO_USER', '')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', '')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', '')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', '')
MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@circle.8oqz5x7.mongodb.net/?retryWrites=true&w=majority&appName=Circle"
