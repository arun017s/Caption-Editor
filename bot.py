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

# experiment
async def get_size(size):
    p=size/1048597
    if p>1000:
         c=round(p/1000, 2)
         filezize=f"{c} GB"
    else:
         c=round(p, 2)
         filezize=f"{c} MB"
    return filezize

async def get_caption(name):
    if "_" in name:
        newcap=name.replace("_", " ") 
    elif "." in name:
        newcap=name.replace(".", " ")
    else:
        newcap=name
    return newcap


bot.on_message(filters.channel & filters.document) #add more filters if you want.
async def caption(bot, message):
    await message.edit(CAPTION.format(name=get_caption(message.document.file_name)    
                                           size=get_size(message.document.file_size))
                      )


bot.run()
