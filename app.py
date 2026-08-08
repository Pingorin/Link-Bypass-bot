import threading
import asyncio
import gradio as gr
from bot import start_telegram_bot
from info import API_ID, API_HASH, BOT_TOKEN

# Background mein bot run karne ka function
def run_bot_in_background():
    # Naya event loop create karna zaroori hai thread ke liye
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_telegram_bot()

# Agar info.py se details mil gayi hain, toh bot ko thread mein start karo
if API_ID and API_HASH and BOT_TOKEN:
    threading.Thread(target=run_bot_in_background, daemon=True).start()
else:
    print("⚠️ API Variables missing hain! Hugging Face ke Secrets mein add karein.")

# Hugging Face ko active rakhne ke liye dummy UI
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Link Bypass Bot Active")
    gr.Markdown("Yeh page sirf server ko zinda rakhne ke liye hai. Bot background mein smoothly chal raha hai. Aap Telegram par jaa kar bot ko use kar sakte hain.")

# Hugging face default port 7860 par app launch karega
demo.launch(server_name="0.0.0.0", server_port=7860)
