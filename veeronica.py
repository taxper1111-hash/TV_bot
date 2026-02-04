import os
import random
import discord
from discord.ext import commands, tasks

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

cute_messages = [
    "veeronica 在這裡 ✨",
    "今天也要有光彩的一天喔 🌸",
    "不要太累了，我有看到你喔 🤍",
    "這個伺服器因為你而亮起來了 ✨",
    "我會陪著大家的，不用擔心 💫",
    "欸嘿～我出現了！"
]

@bot.event
async def on_ready():
    print("veeronica is online")
    if not random_chat.is_running():
        random_chat.start()

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"歡迎 {member.mention} ✨ 我是 veeronica，很高興見到你 🌸")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user.mentioned_in(message):
        replies = [
            "嗯？你叫我嗎 ✨",
            "我在喔～怎麼啦 🌸",
            "嘿嘿，被注意到了 🤍",
            "我有聽到你的聲音 💫"
        ]
        await message.channel.send(random.choice(replies))

    await bot.process_commands(message)

@tasks.loop(minutes=30)
async def random_chat():
    for guild in bot.guilds:
        channel = guild.system_channel
        if channel is not None:
            await channel.send(random.choice(cute_messages))

@bot.command()
async def hello(ctx):
    await ctx.send("你好呀 ✨ 我是 veeronica，很高興認識你 🌸")

@bot.command()
async def mood(ctx):
    moods = [
        "今天是閃閃發光的心情 ✨",
        "有點慵懶，但還是很溫柔 🌸",
        "超級可愛模式中 🤍",
        "安靜地陪著大家 💫"
    ]
    await ctx.send(random.choice(moods))

@bot.command()
async def cheer(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("你本身就很棒了喔 ✨")
    else:
        await ctx.send(f"{member.mention} 要加油喔 🌸 veeronica 站在你這邊 🤍")

bot.run(TOKEN)

