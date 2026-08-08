import logging
import requests
import asyncio
from pyrogram import Client, filters
from info import API_ID, API_HASH, BOT_TOKEN, START_IMAGE

logging.basicConfig(level=logging.INFO)

# In_memory=True rakha gaya hai taaki HF storage error na aaye
bot_client = Client(
    "link_bypass_bot",
    api_id=int(API_ID) if API_ID else 0,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

@bot_client.on_message(filters.command("start"))
async def start_command(client, message):
    caption_text = "Link bypass Bot live"
    
    try:
        await message.reply_photo(
            photo=START_IMAGE,
            caption=caption_text
        )
    except Exception:
        await message.reply_text(f"{caption_text}")

@bot_client.on_message(filters.text & ~filters.command(["start"]))
async def bypass_handler(client, message):
    url = message.text.strip()
    
    if not url.startswith("http"):
        await message.reply_text("⚠️ Kripya ek valid URL bhejein.")
        return

    msg = await message.reply_text("🔄 Process kiya ja raha hai...")

    try:
        response = requests.get(url, allow_redirects=True, timeout=10)
        final_url = response.url
        
        await msg.edit_text(
            f"✅ **Process Complete!**\n\n"
            f"🔗 **Original:** {url}\n"
            f"🚀 **Bypassed:** {final_url}"
        )
    except Exception as e:
        await msg.edit_text(f"❌ Error aaya: {str(e)}")

# ==========================================
# SAFE BACKGROUND LOOP (Anti-Crash Fix)
# ==========================================
async def main_loop():
    try:
        await bot_client.start()
        print("✅ Telegram Bot Successfully Start Ho Gaya Hai!")
        
        # Bot ko zinda rakhne ke liye infinite loop (bina system signals ke)
        while True:
            await asyncio.sleep(3600)
    except Exception as e:
        print(f"❌ Bot Error: {e}")

# Yeh function app.py call karega
def start_telegram_bot():
    print("Starting Telegram Bot Background Process...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main_loop())
