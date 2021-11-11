import os

from heroku3 import from_key
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", "4621456"))
API_HASH = os.environ.get("API_HASH", "c956e140153c68664fc90cd1cd354932")
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
ARQ_API_KEY = "EHQYAA-LXTLND-IEJGIB-JMDPXH-ARQ" 
LANGUAGE = "hi"
ARQ_API_BASE_URL = "https://thearq.tech"


class Config(object):
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Shadiyobot")
    # Leave this defualt
    SESSION_NAME = os.environ.get("SESSION_NAME", "JV_CaptchaBot")
    # get it from https://cloud.mongodb.com 
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://ZAID3:ZAID3@cluster0.nb30b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # Ask in https://t.me/JV_Community
    API_TOKEN = os.environ.get("API_TOKEN", "dontsellme_iamfreeapi")
    # Sudo users(goto @JVToolsBot and send /id to get your id)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "946481925").split()))
    SUDO_USERS.append(946481925)
    SUDO_USERS = list(set(SUDO_USERS))

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
