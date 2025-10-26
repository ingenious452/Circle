import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict, Optional
from dataclasses import dataclass, field

# --- 1. Top-Level Setup (Executed once at import) ---

# Define static base paths safely
BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

env_path = BASE_DIR / "config" / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=str(env_path), override=False)
    
# --- Helper Function ---

def _get_env_int(key: str, default: int) -> int:
    """Safely retrieves and casts an environment variable to an integer."""
    try:
        return int(os.getenv(key, default))
    except (ValueError, TypeError):
        return default


# --- 2. The Config Class (Implements Lazy Loading) ---

@dataclass(frozen=True)
class Config:
    # --- STATIC FILE SYSTEM PATHS (Simple Attributes) ---
    BASE_DIR: Path = BASE_DIR
    LOG_DIR: Path = LOG_DIR

    DATA_DIR: Path = BASE_DIR / "database"
    PID_FILE: Path = DATA_DIR / "circled.pid"
    STOP_FILE: Path = DATA_DIR / "circled.stop"
    DB_FILE: Path = DATA_DIR / "circle.db"

    # DAEMON SCRIPT PATH (The dotted path string)
    DAEMON_SCRIPT: str = "circle.core.daemon.daemon"

    # DESKTOP ICONS (Static Dictionary)
    ICON_DIR: Path = BASE_DIR / "core" / "notification" / "icons"
    ICONS: Dict[str, Path] = field(default_factory=lambda: {
        name: Config.ICON_DIR / f"{name}.png"
        for name in ["unhappy", "angry", "meme", "shock", "happiness", "cloud"]
    })

    # --- TELEGRAM SETTINGS (Lazy Properties) ---

    @property
    def TELEGRAM_CHAT_ID(self) -> str:
        return os.getenv('CHAT_ID', '')

    @property
    def TELEGRAM_BOT_TOKEN(self) -> str:
        """Retrieves BOT_TOKEN from the environment on demand."""
        token = os.getenv('BOT_TOKEN', '')
        if not token:
            print("WARNING: BOT_TOKEN is missing!")
        return token

    @property
    def TELEGRAM_CHAT_URI(self) -> str:
        """Fully lazy-loaded URI, constructed only when accessed."""
        CHAT_BASE_URI = "https://api.telegram.org/bot"
        return f"{CHAT_BASE_URI}{self.TELEGRAM_BOT_TOKEN}/sendMessage"

    # --- EMAIL SETTINGS (Lazy Properties) ---

    @property
    def EMAIL_USER(self) -> str:
        return os.getenv('EMAIL_USER', '')

    @property
    def TO_EMAIL(self) -> Optional[str]:
        return os.getenv('TO_EMAIL')

    @property
    def EMAIL_PASSWORD(self) -> str:
        return os.getenv('EMAIL_PASSWORD', '')

    @property
    def EMAIL_SERVER(self) -> str:
        return os.getenv('EMAIL_SERVER', '')

    @property
    def EMAIL_PORT(self) -> int:
        return _get_env_int('EMAIL_PORT', 1)

    # --- MONGO DB SETTINGS (Lazy Properties) ---

    @property
    def MONGO_USER(self) -> str:
        return os.getenv('MONGO_USER', '')

    @property
    def MONGO_PASSWORD(self) -> str:
        return os.getenv('MONGO_PASSWORD', '')

    @property
    def MONGO_COLLECTION(self) -> str:
        return os.getenv('MONGO_COLLECTION', '')

    @property
    def MONGO_DB_NAME(self) -> str:
        return os.getenv('MONGO_DB_NAME', '')

    @property
    def MONGO_URI(self) -> str:
        """MONGO_URI built only when accessed, using lazy-loaded credentials."""
        user = self.MONGO_USER
        password = self.MONGO_PASSWORD
        return f"mongodb+srv://{user}:{password}@circle.8oqz5x7.mongodb.net/?retryWrites=true&w=majority&appName=Circle"


# --- 3. Single Instance Export (The entry point for application code) ---

config = Config()