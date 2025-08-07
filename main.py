import discord
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Cargar COGs
cogs = ["cogs.comunidad", "cogs.niveles", "cogs.packs", "cogs.verificacion", "cogs.bienvenida", "cogs.moderacion"]
for cog in cogs:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

bot.run(TOKEN)