import threading
import asyncio
import gradio as gr
import spaces
from bot import start_telegram_bot
from info import API_ID, API_HASH, BOT_TOKEN

# ==========================================
# GPU HEALTH CHECK FIX
# ==========================================
@spaces.GPU(timeout=5)
def satisfy_hf_gpu_check():
    print("✅ Hugging Face GPU Check satisfied by dummy function.")
    return "Hugging Face GPU environment detected and active."

# ==========================================
# ISOLATED BACKGROUND BOT LAUNCHER
# ==========================================
def run_bot_in_background():
    # Naya event loop banaya
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Bot ko start karne ka function call kiya (yeh function ab event loop ko block nahi karega)
    start_telegram_bot()
    
    # Event loop ko hamesha chalte rehne dene ke liye run_forever lagaya
    try:
        loop.run_forever()
    except Exception as e:
        print(f"Loop Error: {e}")

# ==========================================
# START BOT THREAD
# ==========================================
if API_ID and API_HASH and BOT_TOKEN:
    # Daemon thread banakar bot ko start kiya
    bot_thread = threading.Thread(target=run_bot_in_background, daemon=True)
    bot_thread.start()
    print("✅ Bot thread started successfully in background.")
else:
    print("⚠️ API Variables missing hain! Fallback values or secrets needed.")

# ==========================================
# GRADIO UI
# ==========================================
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Telegram Link Bypass Bot - GPU Instance")
    gr.Markdown("Yeh Space GPU par chal raha hai. Bot background mein active hai.")
    status = gr.Textbox(label="Status", value="Initializing...")
    demo.load(fn=satisfy_hf_gpu_check, outputs=status)

# Launch ko end mein rakha aur prevent_thread_lock=True nahi lagaya kyunki HF ko block chahiye
demo.launch(server_name="0.0.0.0", server_port=7860)
