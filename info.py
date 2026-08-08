import os

# os.environ.get("SECRET_NAME", "HARDCODED_VALUE")
# Agar Hugging Face par secret hai, toh wo use hoga. Agar nahi hai, toh in quotes "" ke andar wali value use hogi.

API_ID = os.environ.get("API_ID", "20638104") 
API_HASH = os.environ.get("API_HASH", "6c884690ca85d39a4c5ad7c15b194e42")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7718312636:AAG_cLNQRncu3LssN9UKe13ricM-8_fo4kU")
START_IMAGE = os.environ.get("START_IMAGE", "https://telegra.ph/file/4e8b3f2390a184e9185a7.jpg")
