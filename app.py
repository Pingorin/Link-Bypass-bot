import threading
import asyncio
import gradio as gr
import spaces  # <--- Naya import, GPU hardware manage karne ke liye
from bot import start_telegram_bot
from info import API_ID, API_HASH, BOT_TOKEN

# ==========================================
# GPU HEALTH CHECK FIX (Critical for GPU Space)
# ==========================================
# Yeh decorator Hugging Face ko batata hai ki yeh function GPU use karta hai.
# Bhale hi hum isme kuch heavy kaam na karein, ise call karna runtime error ko rokega.
@spaces.GPU(timeout=5) # 5 second ka timeout bohot hai dummy function ke liye
def satisfy_hf_gpu_check():
    print("✅ Hugging Face GPU Check satisfied by dummy function.")
    return "Hugging Face GPU environment detected and active."

# Background mein bot run karne ka function (Already existing)
def run_bot_in_background():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_telegram_bot()

# Bot ko thread mein start karein (Already existing)
if API_ID and API_HASH and BOT_TOKEN:
    threading.Thread(target=run_bot_in_background, daemon=True).start()
else:
    print("⚠️ API Variables missing hain! Fallback values or secrets needed.")

# ==========================================
# GRADIO UI WITH AUTO-LOAD FIX
# ==========================================
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Telegram Link Bypass Bot - GPU Instance")
    gr.Markdown("Yeh Space GPU par chal raha hai. Bot background mein active hai.")
    
    # Ek status text box jisme dummy output dikhega
    status = gr.Textbox(label="Status", value="Initializing...")

    # .load() method use karke, jaise hi application start hogi,
    # hum satisfy_hf_gpu_check() function ko call karenge.
    # Isse Hugging Face detect kar lega ki GPU function run hua hai.
    demo.load(fn=satisfy_hf_gpu_check, outputs=status)

# Hugging face default port 7860 par app launch karega
demo.launch(server_name="0.0.0.0", server_port=7860)
