import asyncio
import discord
from discord.ext import commands, tasks

f_ = open("config.txt", "r")
f = f_.read()
f_.close()

config = {}

f = f.splitlines()

for a in f:
    values = a.split("=")
    config[values[0]] = values[1]

ffmpeg_options = {
    'options': '-vn'
}

bot = commands.Bot(command_prefix=commands.when_mentioned, description='play a sound in a voice channel controlled by a reaction')
bot.remove_command("help")
bot.channel = int(config["channel"])
bot.message = int(config["message"])
bot.emoji = int(config["emoji"])
bot.file = config["file"]

@bot.event
async def on_ready():
    ch = bot.get_channel(bot.channel)

    try:
        m = await ch.fetch_message(bot.message)
        e = bot.get_emoji(bot.emoji)
        await m.add_reaction(e)
        print(f"""Ready as {bot.user} with these options:

• Channel: {ch.name}
• Message: {str(m.content)[:15]}...
• Emoji: {e.name}
• File: {bot.file}

You can invite me to your server with this link: {discord.utils.oauth_url(bot.user.id, permissions = discord.Permissions(permissions = 8))}
""")
    except:
        print(f"""Ready as {bot.user}:

You can invite me to your server with this link: {discord.utils.oauth_url(bot.user.id, permissions = discord.Permissions(permissions = 8))}
""")
    
@bot.event 
async def on_raw_reaction_add(payload):
    ch = bot.get_channel(bot.channel)
    msg = await ch.fetch_message(bot.message)
    if payload.message_id == bot.message:
        if payload.emoji.id == bot.emoji:
            try:
                ctx = await bot.get_context(msg)
                member = ctx.guild.get_member(payload.user_id)
                
                if ctx.voice_client is None:
                    if member.voice:
                        await member.voice.channel.connect()
                    else:
                        if member == ctx.guild.me:
                            return
                        await msg.remove_reaction(bot.get_emoji(bot.emoji), member)
                        return
                
                query = bot.file

                v = ctx.voice_client

                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
                v.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

            except Exception as e:
                print(e)

@bot.event 
async def on_raw_reaction_remove(payload):
    ch = bot.get_channel(bot.channel)
    msg = await ch.fetch_message(bot.message)
    if payload.user_id == bot.user.id:
        await msg.add_reaction(bot.get_emoji(bot.emoji))
        return
    if payload.message_id == bot.message:
        if payload.emoji.id == bot.emoji:
            ctx = await bot.get_context(msg)

            if ctx.voice_client is None:
                return

            await ctx.voice_client.disconnect()

bot.run(config["token"])