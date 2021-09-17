import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time

from gtts import gTTS

bot = commands.Bot(command_prefix="!")
# client = discord.Client()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def join(ctx):
    voice = get(bot.voice_clients)
    if voice is not None:
        await ctx.voice_client.disconnect()

    await ctx.author.voice.channel.connect()

    global gTTS
    speech = gTTS(text='บอทอ่านชื่อมาแล้วจ้า', lang="th", slow=False)
    speech.save("audio.mp3")

    time.sleep(1)

    while get(bot.voice_clients) is None:
        time.sleep(1)
    voice = get(bot.voice_clients)

    voice.play(discord.FFmpegPCMAudio('audio.mp3'), after=None)


@bot.command()
async def leave(ctx):
    voice = get(bot.voice_clients)
    if voice is None:
        return

    name_user = ctx.author.display_name
    suffix = "เต่กูออกจากห้อง ไอ้สัส"

    global gTTS
    speech = gTTS(text=name_user + suffix, lang="th", slow=False)
    speech.save("audio.mp3")

    voice.play(discord.FFmpegPCMAudio('audio.mp3'), after=None)
    time.sleep(5)
    await ctx.voice_client.disconnect()


@bot.command()
async def tts(ctx, arg, arg2="th"):
    voice = get(bot.voice_clients)
    if voice is None:
        await ctx.send(f"{ctx.author.mention} ชวนเราเข้าห้องก่อนสิ (!join)")
    if len(arg) > 20:
        await ctx.send(f"{ctx.author.mention} ยาวไปไอ้สัส")
        return

    voice = get(bot.voice_clients)
    if voice is None:
        return

    prefix = ctx.author.display_name + "พูดว่า"

    global gTTS
    speech = gTTS(text=prefix+arg, lang=arg2, slow=False)
    speech.save("audio.mp3")

    voice = get(bot.voice_clients)

    voice.play(discord.FFmpegPCMAudio('audio.mp3'), after=None)

@bot.command()
async def awt(ctx):
    voice = get(bot.voice_clients)
    if voice is None:
        await ctx.send(f"{ctx.author.mention} ชวนเราเข้าห้องก่อนสิ (!join)")

    voice = get(bot.voice_clients)
    if voice is None:
        return

    global gTTS
    speech = gTTS(text="atomic war time", lang="es-us", slow=False)
    speech.save("audio.mp3")

    voice = get(bot.voice_clients)

    voice.play(discord.FFmpegPCMAudio('audio.mp3'), after=None)

@bot.command()
async def cw(ctx, arg):
    voice = get(bot.voice_clients)
    if voice is None:
        await ctx.send(f"{ctx.author.mention} ชวนเราเข้าห้องก่อนสิ (!join)")
        return

    voice.play(discord.FFmpegPCMAudio(f'chatwheel/{arg}.mp3'), after=None)
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.5
    # await ctx.message.delete()


@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot == True:
        return

    voice = get(bot.voice_clients)
    if voice is None:
        return

    name_user = member.display_name

    if before.channel != voice.channel and after.channel == voice.channel:
        suffix = " เข้ามาในห้อง"
    elif before.channel == voice.channel and after.channel != voice.channel:
        suffix = " ออกจากห้อง"
    else:
        return

    global gTTS
    speech = gTTS(text=name_user + suffix, lang="th", slow=False)
    speech.save("audio.mp3")

    time.sleep(2)

    voice.play(discord.FFmpegPCMAudio('audio.mp3'), after=None)


bot.run('ODg1ODMxODkzODIyNjA3NDIw.YTsxPQ.Pnmu-Tp_HN8zrFm3v3eynal25ss')
