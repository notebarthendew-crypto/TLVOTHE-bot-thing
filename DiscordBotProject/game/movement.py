# the main code for moving around the map

from discord import app_commands
import discord

from game.player import players, create_player
from game.movement import move_player

GAME_ROLE_ID = 123456789012345678 #i dont have my pc right now to get the role i gotta change this

@bot.tree.command(name="move", description="Move through the train")
@app_commands.describe(direction="front or back")
async def move(interaction: discord.Interaction, direction: str):

    member = interaction.user

    # Check role
    has_role = any(role.id == GAME_ROLE_ID for role in member.roles)

    if not has_role:
        await interaction.response.send_message(
            "You ain't playing.",
            ephemeral=True
        )
        return

    user_id = str(member.id)

    if user_id not in players:
        create_player(user_id)

    result = move_player(players[user_id], direction)

    if result is None:
        await interaction.response.send_message(
            "You can't go that way.",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"You moved to {result}.",
        ephemeral=True
    )
