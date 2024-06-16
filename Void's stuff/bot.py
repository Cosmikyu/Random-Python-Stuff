import discord
from discord.ext import commands

token = input("Bot Token: ")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def deez(ctx):
    await ctx.send('nuts')

bot.run(token)