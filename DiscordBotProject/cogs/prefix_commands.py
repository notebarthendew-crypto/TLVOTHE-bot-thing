from discord import app_commands
import discord

def setup_commands(bot):
    
    @bot.command()
    async def hello(ctx):
        await ctx.send(f"hi {ctx.author.mention}")

    @bot.command()
    async def reply(ctx):
        await ctx.reply("This is a reply. (wow)")
    
    @bot.command()
    async def cheese(ctx):
        await ctx.send("https://tenor.com/view/crowpunk-cheese-challenge-repost-to-cheese-cat-cheese-cat-gif-4123783956472567463")

    @bot.command()
    async def revolver(ctx):
        await ctx.reply(f"Heres a gun"
                       "# <:Revolver:1505709394057494659>")
