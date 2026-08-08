import os

# Hugging Face Secrets se data lega. 
# Agar aap local PC par test kar rahe hain, toh os.environ.get("API_ID", "APNA_ID_YAHAN_DALEIN") kar sakte hain.

API_ID = os.environ.get("API_ID") 
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
