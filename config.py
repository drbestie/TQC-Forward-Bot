from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "12345678")) #fill your api id
    API_HASH = environ.get("API_HASH", "bsdsndabdasdasd") #fill your api hash
    BOT_TOKEN = environ.get("BOT_TOKEN", "1928292929:AAHjdsadadadadadadadadad") #fill your bot token
    BOT_SESSION = environ.get("BOT_SESSION", "techqwikcode") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://techqwikcode:techqwikcode@cluster0.5v7sa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") #fill your mongodb uri
    DATABASE_NAME = environ.get("DATABASE_NAME", "techqwikcode-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "1234567890")) #fill your telegram id
    LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "0")) or None #fill your log channel id but make sure your bot is admin in there and you can also leave it blank if you don't want to log


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []