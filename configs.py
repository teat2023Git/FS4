# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "GreyMatterslinks.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "20eb8456008878c0349fc79d40fb4d1634cccf12")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
Tʜɪs Bᴏᴛ ɪs Cʀᴇᴀᴛᴇᴅ ʙʏ: [𝑴𝒓. 𝑨𝒏𝒐𝒏𝒚𝒎𝒐𝒖𝒔🦠](tg://settings)
  
Repo Credit : [@MeARobo](https://t.me/MeARobo)
 
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent FileStore Bot🔞. \n𝐅𝐈𝐋𝐄 𝐖𝐎𝐍'𝐓 𝐃𝐄𝐋𝐄𝐓𝐄 𝐓𝐈𝐋𝐋 𝐈 𝐃𝐄𝐋𝐄𝐓𝐄 .

Join: @KMZoneOfficial"""
