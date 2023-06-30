from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/b33d8a4bd9b4be47eccef.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/136c76d8fed2d3d27ef22.mp4")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Ghostwasit")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/wasit_go")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5917983447").split()))


FAILED = "https://graph.org/file/b33d8a4bd9b4be47eccef.jpg"
