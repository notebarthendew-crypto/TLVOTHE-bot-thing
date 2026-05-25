from discord.ext import commands

class MessageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        # Ignore bot messages
        if message.author == self.bot.user:
            return

        print(f"{message.author}: {message.content}")

        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(MessageCommands(bot))
