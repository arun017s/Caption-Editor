Edit captions of channel messages

### Variables:
1. `API_ID` : Get From [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `BOT_TOKEN` : Your Telegram Bot Token from [@BotFather](https://t.me/BotFather)
4. `CAPTION` : Caption for messages 

#### CAPTION Fillings
* `{name}` - File Name
* `{size}` - File size

### Deploy on Heroku
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
- Turn on dynos after deployment

### Deploy in your VPS
```sh
git clone https://github.com/Arun-TG/Caption-Editor
cd Caption-Editor
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```

### Credits
* [Pyrogram](https://github.com/pyrogram/pyrogram)
* [Arun](https://t.me/arun_tg)
