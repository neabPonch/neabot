from discord.ext import commands
from discord.ext.commands import MissingRole

import DBstuff
import random

class Quotes(commands.Cog): # extends the commands.Cog class in python
    def __init__(self, bot): # define constructor that receives self/bot
        self.bot = bot # bot will be instance of bot from main


    def cleanquote(self, quote):
        return quote[0][0]


    @commands.command(name='random')
    async def randomquote(self, message):
        query = '''SELECT quote FROM quotes
        ORDER BY RAND()
        LIMIT 1'''
        randomQuote = DBstuff.DBstuff.dbquery(query=query)
        await message.send(self.cleanquote(randomQuote))

    @commands.command(name='quoteadd')
    @commands.has_role('neab')
    async def addquote(self, message):
        query = 'INSERT INTO quotes(quote, addedby) VALUES (%s, %s)'
        user = message.author.name
        string = message.message.content[10:]
        newquotevalues = (string, user)
        newquotenumber = DBstuff.DBstuff.dbquery(query=query, newquote=newquotevalues)
        await message.send('quote {} added'.format(newquotenumber))

    @commands.command(name='quotedelete')
    @commands.has_role('Admin')
    async def deletequote(self, message):
        string = message.message.content
        query = 'DELETE FROM quotes WHERE id = (%s)'
        quotenumber = [int(s) for s in string.split() if s.isdigit()][0]
        DBstuff.DBstuff.dbquery(query=query, quotenumber=quotenumber)
        await message.send('quote {} deleted'.format(quotenumber))

    @deletequote.error
    async def deletequoteerror(self, message, error):
        if isinstance(error, MissingRole):
            await message.send("You're too much of a pleb. STOP. THE. COUNT.")

    @commands.command(name='quote')
    async def callquote(self, message):
        query = "SELECT quote FROM quotes WHERE id = (%s)"
        string = message.message.content
        try:
            quotenumber = [int(s) for s in string.split() if s.isdigit()][0]
            try:
                fullquote = DBstuff.DBstuff.dbquery(query=query, quotenumber=quotenumber)
                await message.send(self.cleanquote(fullquote))
            except:
                await message.send("That quote doesn't exist, you fuck.")
        except:
            await message.send(
                "Put a number after the quote, fucktard. Or type !random for a badass random neab quote.")

    @commands.command(name='quotefind')
    async def quotefind(self, message):
        query = "SELECT quote FROM quotes WHERE quote LIKE (%s)"
        findstring = '%' + message.message.content[11:] + '%'
        try:
            findquote = DBstuff.DBstuff.dbquery(query=query, quotenumber=findstring)
            finalfindquote = random.choice(findquote)
            await message.send(finalfindquote[0])
        except:
            await message.send("Um, you broke me.")


def setup(bot):
    bot.add_cog(Quotes(bot)) # instantiates Quotes cog