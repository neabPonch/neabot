from discord.ext import commands

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message): # self refers to instance of class itself
        if '69' in message.content:
            await message.channel.send('nice')
        elif 'bye' in message.content:
            await message.channel.send('beat it, neab')


def setup(bot):  # required for all Cogs
    bot.add_cog(Listener(bot))  # instantiates Listener Cog
