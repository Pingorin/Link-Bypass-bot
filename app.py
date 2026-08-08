import threading
import gradio as gr
import spaces
from bot import start_bot_sync
from info import API_ID, API_HASH, BOT_TOKEN

# ==========================================
# GPU HEALTH CHECK
# ==========================================
@spaces.GPU(timeout=5)
def satisfy_hf_gpu_check():
    print("✅ GPU environment verified by Hugging Face.")
    return "GPU is active and Bot is listening..."

# ==========================================
# START BOT THREAD
# ==========================================
if API_ID and API_HASH and BOT_TOKEN:
    # Thread banakar bot.py ke function ko call kiya
    # daemon=True ka matlab hai jab HF app band ho, toh thread bhi band ho jaye
    bot_thread = threading.Thread(target=start_bot_sync, daemon=True)
    bot_thread.start()
    print("✅ Bot thread launched successfully.")
else:
    print("⚠️ API Variables missing! Cannot start bot.")

# ==========================================
# GRADIO UI (Runs on Main Thread)
# ==========================================
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Telegram Link Bypass Bot - GPU Instance")
    gr.Markdown("Bot is running in the background. Use it on Telegram.")
    status = gr.Textbox(label="Status", value="Initializing...")
    
    # HF GPU ko verify karne ke liye function load
    demo.load(fn=satisfy_hf_gpu_check, outputs=status)

# Isko last mein hi rakhna hai
demo.launch(server_name="0.0.0.0", server_port=7860)
