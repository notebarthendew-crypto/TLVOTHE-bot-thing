from discord import app_commands
import discord

def setup_commands(bot):

  @bot.tree.command(name="ping")
  async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")
