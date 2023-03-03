#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler


from dotenv import load_dotenv
load_dotenv()
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5652142085:AAFSCxI6oBGjP6BWdmQC1z44eb9U45xWSPg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13886259"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7b6e621b09f2bd60db1bd1bd81c1a6ae")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001579061310"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5937683464"))

#Port
PORT = os.environ.get("PORT", "8080")

#shortlink
SHORTENER_API = "jdisk.cloud"
SHORTENER_SITE = "6521569d4643af31e7ea0699fe7bf0a82b1dc713"

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://siddarthceo:siddarthceo@filesharebot.v8mwdbb.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharebot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001892307076"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5937683464 1174794359").split())]
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.") 

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.extend((OWNER_ID, 1250450587))
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
