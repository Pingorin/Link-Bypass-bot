import logging
import requests
from pyrogram import Client, filters
from info import API_ID, API_HASH, BOT_TOKEN, START_IMAGE

# Bypasser file se dono functions import kar rahe hain
from bypasser import bypass_adlinkfly, decode_base64_url

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot_client = Client(
    "link_bypass_bot",
    api_id=int(API_ID) if API_ID else 0,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

@bot_client.on_message(filters.command("start"))
async def start_command(client, message):
    caption_text = "Link bypass Bot live 🚀\n\nMujhe koi bhi link bhejiye aur main uske redirects bypass karke original link nikal dunga."
    try:
        await message.reply_photo(photo=START_IMAGE, caption=caption_text)
    except Exception as e:
        logger.error(f"Image Error: {e}")
        await message.reply_text(caption_text)

@bot_client.on_message(filters.text & ~filters.command(["start"]))
async def bypass_handler(client, message):
    url = message.text.strip()
    
    if not url.startswith("http"):
        await message.reply_text("⚠️ Kripya ek valid URL bhejein (http:// ya https:// se shuru hone wala).")
        return

    msg = await message.reply_text("🔄 Process kiya ja raha hai... (Kripya thoda wait karein)")

    # 🟢 Step 1: Base64 Check (Agar link mein final URL chupa hai)
    base64_url = decode_base64_url(url)
    if base64_url:
        await msg.edit_text(
            f"✅ **Base64 Decode Successful!**\n\n"
            f"🔗 **Original:** `{url}`\n\n"
            f"🚀 **Final Destination:** `{base64_url}`",
            disable_web_page_preview=True
        )
        return

    # 🟢 Step 2: Adlinkfly Check (Agar shortxlinks jaisa ad-network hai)
    # Aap yahan aur bhi adlinkfly domains add kar sakte hain
    adlinkfly_domains = ["shortxlinks.in", "rocklinks.net", "gplinks.in"] 
    is_adlinkfly = any(domain in url for domain in adlinkfly_domains)

    try:
        if is_adlinkfly:
            final_url = bypass_adlinkfly(url)
            if final_url:
                await msg.edit_text(
                    f"✅ **Advanced Bypass Successful!**\n\n"
                    f"🔗 **Original:** `{url}`\n\n"
                    f"🚀 **Final Destination:** `{final_url}`",
                    disable_web_page_preview=True
                )
            else:
                await msg.edit_text("❌ Bypass fail ho gaya. Ya toh is link par Captcha laga hai, ya server down hai.")
        
        else:
            # 🟢 Step 3: Normal HTTP Redirect (Bit.ly, Tinyurl etc.)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
            response = requests.get(url, headers=headers, allow_redirects=True, timeout=15)
            final_url = response.url
            
            if final_url == url:
                await msg.edit_text("ℹ️ Ye link pehle se hi direct hai, isme koi redirect nahi mila (Ya ye shortener humare database me nahi hai).")
            else:
                await msg.edit_text(
                    f"✅ **Process Complete!**\n\n"
                    f"🔗 **Original:** `{url}`\n\n"
                    f"🚀 **Bypassed:** `{final_url}`",
                    disable_web_page_preview=True
                )
    except requests.exceptions.Timeout:
        await msg.edit_text("❌ Timeout Error: Website load hone mein bahut time le rahi hai.")
    except Exception as e:
        await msg.edit_text(f"❌ Error aaya: {str(e)}")

# ==========================================
# START BOT
# ==========================================
if __name__ == "__main__":
    logger.info("Initializing Telegram Bot...")
    try:
        bot_client.run()
    except Exception as e:
        logger.error(f"Bot failed to start: {e}")
