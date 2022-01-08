# (C) Arunkumar Shibu 

# Edit captions of channel messages
# Maybe useful for movie channels 

import os
from pyrogram import Client, filters

CAPTION = os.environ.get("CAPTION")

bot = Client(session_name="caption-editor",
             api_id=int(os.environ.get("API_ID")),
             api_hash=os.environ.get("API_HASH"),
             bot_token=os.environ.get("BOT_TOKEN"))

#experiment #fail
async def get_size(size):
    p=size/1048597           #size in MB
    if p>1024:
         c=round(p/1024, 2)
         filezize=f"{c} GB"
    elif p>1:
         c=round(p, 2)
         filezize=f"{c} MB"
    else:
         c=round(size/1024, 1)
         filezize=f"{c} KB"
    return filezize

async def get_caption(name):
    if "_" in name:
        newcap=name.replace("_", " ")     
    else:
        newcap=name
    return newcap

@bot.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply(f"Hello {message.from_user.mention},\nI will edit channel message's captions.\nAdd me to your channel with necessary permissions.")

@bot.on_message(filters.channel & filters.document) #add more filters if you want.
async def caption(bot, message):
   try:
       await message.edit(CAPTION.format(name=await get_caption(message.document.file_name),    
                                         size=await get_size(message.document.file_size))
                          )
   except Exception as e:
       print(e)


bot.run()
