from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/19ca5a3150d7b2416d3c1.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/19ca5a3150d7b2416d3c1.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/A_S_A_33")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/D_Z_A_R")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6456641797").split()))


FAILED = "https://graph.org/file/19ca5a3150d7b2416d3c1.jpg"
