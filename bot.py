import os

import pyrogram

from pyrogram import Client, filters

# Get your APP_ID and API_HASH from https://my.telegram.org/

app_id = "22205158"

api_hash = "4fd96f16abab38cea55da11166fb4184"

# Create a Telegram bot

bot = Client("my_bot", api_id=app_id, api_hash=api_hash)

# Define a command to upload files

@bot.on(filters.command("upload"))

async def upload(client, message):

    # Get the file path from the message

    file_path = message.text

    # Upload the file to Mega

    mega = Mega()

    mega.login("YOUR_MEGA_EMAIL", "YOUR_MEGA_PASSWORD")

    mega.upload(file_path)

    # Send a message to the user confirming that the file was uploaded

    await message.reply("File uploaded successfully!")

# Run the bot

bot.run()

