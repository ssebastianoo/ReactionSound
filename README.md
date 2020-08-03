# ReactionSound
*Play a sound in a Discord voice channel by reacting to a message*

**The bot is not public, you need to self host it to use it**

![example](https://elon-musk.is-inside.me/udPv5lFh.gif)

## How to host the bot
- Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create an application
- Name it however you want
![create application](https://elon-musk.is-inside.me/iSf0cExt.png)
- On the left press **Bot** and then **Add Bot**
- Copy the token, we'll need it later
- Download the latest version of [Python](https://www.python.org/downloads/) and select **Add to path** during the installation
- Open your terminal (or [cmd](https://www.quora.com/How-do-I-open-terminal-in-windows#:~:text=Press%20%22Win%2DR%2C%22,session%20using%20just%20your%20keyboard.&text=Click%20the%20%22Start%20%3E%3E%20Program,session%20using%20just%20your%20mouse.) on Windows)
- Download [FFmpeg](https://ffmpeg.org/download.html)
- Type `python3 -m pip install -U discord.py[voice]` *(`python` on Windows)*
- Find the project directory [using cd](http://modulesunraveled.com/command-line-beginners/moving-and-out-directories-cd-command)
- Put inside the folder your sound file
- Open `config.txt` and set the values with the bot token, the id of the channel where your message is, the id of the message, the id of the emoji, the name of the file (like `sound.mp3`), this is an example:
```
token=NjkxMjYyMDYzNzc5MjUwMjA3.XndZ9w.IiQ1UYAP26r8VDD3rbkf84SXqQM
channel=739627727820161244
message=739627991553802290
emoji=739627965423550514
file=sound.mp3
```
- Run `python3 main.py` *(or `python main.py` if you're on Windows)*
- A link will appear om the terminal, use it to invite the bot to your server
- It's all done!
