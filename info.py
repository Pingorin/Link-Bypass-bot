import os

# Hugging Face Secrets se data lega. 
# Agar aap local PC par test kar rahe hain, toh os.environ.get("API_ID", "APNA_ID_YAHAN_DALEIN") kar sakte hain.

API_ID = os.environ.get("20638104") 
API_HASH = os.environ.get("6c884690ca85d39a4c5ad7c15b194e42")
BOT_TOKEN = os.environ.get("7718312636:AAG_cLNQRncu3LssN9UKe13ricM-8_fo4kU")
