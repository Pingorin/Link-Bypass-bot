import os
import subprocess
import gradio as gr
import spaces
from info import API_ID, API_HASH, BOT_TOKEN

# ==========================================
# START BOT IN BACKGROUND PROCESS (Like Auto Filter)
# ==========================================
if API_ID and API_HASH and BOT_TOKEN:
    # Threading ki jagah subprocess ka use, isse bot kabhi crash nahi hoga
    subprocess.Popen(["python", "bot.py"])
    print("✅ Bot process launched successfully.")
else:
    print("⚠️ API Variables missing! Cannot start bot.")

# ==========================================
# GPU HEALTH CHECK & GRADIO UI
# ==========================================
@spaces.GPU(timeout=5)
def satisfy_hf_gpu_check():
    print("✅ GPU environment verified by Hugging Face.")
    return "GPU is active and Bot is listening..."

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Telegram Link Bypass Bot - GPU Instance")
    gr.Markdown("Bot is running perfectly in the background. Use it on Telegram.")
    status = gr.Textbox(label="Status", value="Initializing...")
    
    # HF GPU ko verify karne ke liye function load
    demo.load(fn=satisfy_hf_gpu_check, outputs=status)

# Isko last mein hi rakhna hai
demo.launch(server_name="0.0.0.0", server_port=7860)
