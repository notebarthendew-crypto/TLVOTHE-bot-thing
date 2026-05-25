import discord
from discord.ext import commands
from discord import app_commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents)

from cogs.commands import setup_commands as setup_slash_commands
from cogs.prefix_commands import setup_commands as setup_prefix_commands
from cogs.game_commands import setup_commands as setup_game_commands
from cogs.message_events import setup_commands as setup_message_events

setup_message_events(bot)
setup_slash_commands(bot)
setup_prefix_commands(bot)
setup_game_commands(bot)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("haha pepee popoo whoah hehehe")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game("Poisoning the food...")
    )

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(
                "Hello! Thank you for inviting me to your server!.\n"
                "...Although I should be somewhere else...."
            )
            break


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
