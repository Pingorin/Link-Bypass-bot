import logging
import requests
from pyrogram import Client, filters
from info import API_ID, API_HASH, BOT_TOKEN, START_IMAGE

logging.basicConfig(level=logging.INFO)

# Pyrogram Client Setup
bot_client = Client(
    "link_bypass_bot",
    api_id=int(API_ID) if API_ID else 0,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot_client.on_message(filters.command("start"))
async def start_command(client, message):
    caption_text = "Link bypass Bot live"
    
    # Try block lagaya hai taaki agar image URL invalid ho toh bot crash na ho
    try:
        await message.reply_photo(
            photo=START_IMAGE,
            caption=caption_text
        )
    except Exception as e:
        # Agar image load hone mein koi dikkat aaye, toh sirf text bhej dega
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

# Yeh function app.py se call hoga bot ko start karne ke liye
def start_telegram_bot():
    print("Starting Telegram Bot...")
    bot_client.run()
