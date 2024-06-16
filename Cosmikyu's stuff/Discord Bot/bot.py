#This script needs working on, probably going to fix it later on

import discord
from discord.ext import commands
import os
import base64

# Get the directory path where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))
TOKEN_FILE = os.path.join(script_dir, 'token.txt')

def encode_token(token):
    token_bytes = token.encode('utf-8')
    base64_bytes = base64.b64encode(token_bytes)
    return base64_bytes.decode('utf-8')

def decode_token(encoded_token):
    base64_bytes = encoded_token.encode('utf-8')
    token_bytes = base64.b64decode(base64_bytes)
    return token_bytes.decode('utf-8')

def get_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as file:
            encoded_token = file.read().strip()
        if encoded_token:
            return decode_token(encoded_token)
    
    token = input("Please enter your bot token: ")
    encoded_token = encode_token(token)
    with open(TOKEN_FILE, 'w') as file:
        file.write(encoded_token)
    return token

token = get_token()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def userinfo(ctx, *, username: str = None):
    if username is None:
        await ctx.send("Please provide a username (and discriminator) in the format `username#discriminator`.")
        return
    
    discriminator = None
    
    if '#' in username:
        username, discriminator = username.split('#')
    
    user = discord.utils.get(bot.users, name=username, discriminator=discriminator)
    
    if user is None:
        if ctx.guild:
            for member in ctx.guild.members:
                if member.name == username and (discriminator is None or member.discriminator == discriminator):
                    user = member
                    break
    
    if user is None:
        await ctx.send("User not found.")
        return
    
    if isinstance(user, discord.Member):
        embed = discord.Embed(title="User Info", color=discord.Color.blue())
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="Bot?", value=user.bot, inline=True)
        embed.add_field(name="Created At", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    else:
        embed = discord.Embed(title="User Info", color=discord.Color.blue())
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="Bot?", value=user.bot, inline=True)
        embed.add_field(name="Created At", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    
    await ctx.send(embed=embed)

bot.run(token)