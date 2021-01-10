from discord.ext import commands
import random


class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='catjam')
    async def catjam(self, message):
        await message.send('https://cdn.discordapp.com/emojis/754451737762595017.gif?v=1')

    @commands.command(name='athonking')
    async def athonking(self, message):
        await message.send('https://cdn.discordapp.com/emojis/512632629732835344.gif?v=1')

    @commands.command(name='emojilist')
    async def emojilist(self, message):
        emoji = list(message.get_all_emojis())
        await message.send(emoji)

    @commands.command(name='gay')
    @commands.has_role('neab')
    async def gay(self, message):
        user = message.author.name
        gaypercent = random.randint(0, 101)
        await message.send('{} you are {}% gay! Let\'s fuck, you sexy beast.'.format(user, gaypercent))


def setup(bot):  # required for all Cogs
    bot.add_cog(MiscCommands(bot))  # instantiates MiscCommands Cog
