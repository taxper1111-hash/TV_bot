import discord
from discord.ext import commands, tasks
import random
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

HELLO_LINES = [
    "嗨嗨～我是 veeronica ✨ 很高興見到你！",
    "你好呀～今天也要開開心心的喔 🌸",
    "欸嘿～我來陪你們啦 🐣"
]

HUG_LINES = [
    "（輕輕抱住）給你一個溫柔的抱抱 🤍",
    "抱抱時間到～希望你能感覺好一點 🫶",
    "來來來～不管發生什麼，我都在喔 🌈"
]

CHEER_LINES = [
    "你今天能走到這裡，已經很棒了 ✨",
    "別小看自己，你其實很努力 🌱",
    "就算慢一點，也是在前進喔 💕"
]

MOOD_BOOST_LINES = [
    "欸欸～大家深呼吸一下好嗎 🌸",
    "氣氛有點亂，我來加點可愛 ✨",
    "沒事沒事～我們慢慢來 🐣"
]

LIGHT_MESSAGES = [
    "🌈 小提醒：記得喝水喔！",
    "✨ 你們知道嗎？這個伺服器其實很溫暖。",
    "🌸 如果你今天很累，這裡可以休息一下喔。",
    "🐣 能待在這裡的你，本身就很溫柔。"
]

def allowed_channel(obj):
    return obj.channel.id == CHANNEL_ID

@bot.event
async def on_ready():
    print(f"veeronica online as {bot.user}")
    if not light_event.is_running():
        light_event.start()

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if not allowed_channel(message):
        return
    if len(message.content) >= 120:
        if random.random() < 0.15:
            await message.channel.send(random.choice(MOOD_BOOST_LINES))
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    if not allowed_channel(ctx):
        return
    await ctx.send(random.choice(HELLO_LINES))

@bot.command()
async def hug(ctx, member: discord.Member = None):
    if not allowed_channel(ctx):
        return
    if member is None:
        await ctx.send("要抱誰呢～？🥺")
    else:
        await ctx.send(f"{member.mention} {random.choice(HUG_LINES)}")

@bot.command()
async def cheer(ctx):
    if not allowed_channel(ctx):
        return
    await ctx.send(random.choice(CHEER_LINES))

@tasks.loop(minutes=60)
async def light_event():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        if random.random() < 0.4:
            await channel.send(random.choice(LIGHT_MESSAGES))

bot.run(TOKEN)
