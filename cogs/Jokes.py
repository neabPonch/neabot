from discord.ext import commands
from discord.ext.commands import MissingRole
import DBstuff
import random

class Jokes(commands.Cog): # extends the commands.Cog class in python
    def __init__(self, bot): # define constructor that receives self/bot
        self.bot = bot # bot will be instance of bot from main


    def cleanjoke(self, joke):
        return joke[0][0]


    @commands.command(name='joke')
    async def randomjoke(self, message):
        query = '''SELECT body FROM puns
        ORDER BY RAND()
        LIMIT 1'''
        randomJoke = DBstuff.DBstuff.dbjokequery(query=query)
        await message.send(self.cleanjoke(randomJoke))

def setup(bot):
    bot.add_cog(Jokes(bot)) # instantiates Jokes cog