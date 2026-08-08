---
title: Link Bypass Bot
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
---

# 🚀 Telegram Link Bypass Bot

This is a fast and lightweight Telegram Link Bypass Bot built with Python and **Pyrogram**. It is specially designed and structured to be hosted continuously on **Hugging Face Spaces** by running a dummy **Gradio** web server on port `7860` in the foreground while the Telegram bot runs smoothly in the background.

## 📁 Repository Structure

The code is modularized into separate files for better management:

- `info.py` - Manages all environment variables and API credentials.
- `bot.py` - Contains the core Pyrogram Telegram bot logic and link bypass handling.
- `app.py` - The main entry point for Hugging Face. It launches the Gradio UI and starts the bot in a background thread.
- `requirements.txt` - Lists the required Python dependencies (`pyrogram`, `tgcrypto`, `requests`, `gradio`).
- `.github/workflows/sync.yml` - Automates syncing code from GitHub to Hugging Face Spaces.

## 🛠️ Deployment on Hugging Face

1. Create a new **Gradio Space** on your Hugging Face account.
2. Go to your Space's **Settings** > **Variables and secrets**.
3. Add the following **Secrets**:
   - `API_ID`: Your Telegram API ID (get it from my.telegram.org)
   - `API_HASH`: Your Telegram API Hash
   - `BOT_TOKEN`: Your Bot Token (get it from @BotFather)
4. Upload all the files or sync them using the provided GitHub Actions workflow.
5. The Space will automatically build and start running.

## 🔄 Automated GitHub Sync

This repository includes a GitHub Action (`sync.yml`) that automatically pushes code changes to Hugging Face. 
To enable this:
1. Generate an Access Token (with **Write** permission) in your Hugging Face account settings.
2. Go to your GitHub Repository **Settings** > **Secrets and variables** > **Actions**.
3. Create a New repository secret named `HF_TOKEN` and paste your Hugging Face token.

## 💻 Local Testing

If you want to run this bot locally on your computer:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your environment variables locally (or hardcode them temporarily in `info.py`).
4. Run the app: `python app.py`

## 🔮 Future Upgrades
The current file structure supports easy scalability. If you plan to add user tracking, indexing, or caching in the future, you can easily integrate **MongoDB** by creating a separate `database.py` file and connecting it directly to `bot.py`.
