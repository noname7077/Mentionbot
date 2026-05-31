import os
import asyncio
from telethon import TelegramClient, events

API_ID = 35483314             
API_HASH = "ce93f573ff7b23f83d9f55a5f74198ca"   
BOT_TOKEN = "8834699300:AAFOTwOGCt2RoZWhugudAGqALtFRxSck7H4" 

bot = TelegramClient('mentionbot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("👋 Hello! Mai Mention Bot hu. Mujhe apne group me admin banayein, fir mai sabhi members ko tag kar sakta hu.\n\nCommands:\n/all [aapka message] - Sabhi ko tag karne ke liye.")

@bot.on(events.NewMessage(pattern='/all'))
async def mentionall(event):
    if not event.is_group:
        await event.reply("❌ Ye command sirf groups me kaam karegi!")
        return
    
    msg_text = event.pattern_match.string.split(None, 1)
    extra_msg = msg_text[1] if len(msg_text) > 1 else "Suno sabhi!"

    await event.reply("📣 Sabhi members ko mention kiya ja raha hai, kripya dhyan dein!")
    
    mentions = ""
    counter = 0
    
    async for user in bot.iter_participants(event.chat_id):
        if user.bot:
            continue
        
        mentions += f"[{user.first_name}](tg://user?id={user.id}) "
        counter += 1
        
        if counter == 5:
            await bot.send_message(event.chat_id, f"{extra_msg}\n\n{mentions}")
            mentions = ""
            counter = 0
            await asyncio.sleep(2)
            
    if counter > 0:
        await bot.send_message(event.chat_id, f"{extra_msg}\n\n{mentions}")

print("⚡ Mention Bot successfully start ho gaya hai...")
bot.run_until_disconnected()
