from discord.ext import commands
import random
import discord


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

    @commands.command(name='percent')
    @commands.has_role('neab')
    async def percent(self, message):
        user = message.author.name
        percentvalue = random.randint(0, 101)
        messagecontent = message.message.content[9:]
        await message.send('{}, you are {}% {}! Eat shit and die!'.format(user, percentvalue, messagecontent))

    @commands.command(name='pp')
    @commands.has_role('neab')
    async def pp(self, message):
        user = message.author.name
        pplength = round(random.uniform(0, 35), 2)
        await message.send('{}, your penis is {} cm long! Congratulations.'.format(user, pplength))

    @commands.command(name='8ball')
    @commands.has_role('neab')
    async def eightball(self, message):
        user = message.author.name
        eightballchoices = ['don’t count on it.',
                            'it is certain.',
                            'it is decidedly so.',
                            'most likely.',
                            'my reply is no.',
                            'my sources say no.',
                            'outlook not so good.',
                            'outlook good.',
                            'signs point to yes.',
                            'very doubtful.',
                            'without a doubt.',
                            'yes.',
                            'yes – definitely.',
                            'you may rely on it.',
                            'does the pope shit in the woods?',
                            'lol, no.',
                            'ya.',
                            'nah',
                            'fuck yea, breh.']
        answer = random.choice(eightballchoices)
        await message.send('{}, {}'.format(user, answer))

    @commands.command(name='mock')
    @commands.has_role('neab')
    async def mock(self, message):
        lastmessageobj = await message.channel.history(limit=2).flatten()
        lastmessageid = lastmessageobj[1].content.lower()
        count = len(lastmessageid)
        mocktxt1 = ''

        for letter in lastmessageid:
            if count % 2 == 0:
                mocktxt1 = mocktxt1 + letter
                count -= 1
            else:
                mocktxt1 = mocktxt1 + letter.upper()
                count -= 1

        embed = discord.Embed()
        embed.set_image(url='https://imgur.com/I1xDtWl.jpg')
        embed.set_footer(text=mocktxt1)
        await message.send(embed=embed)

def setup(bot):  # required for all Cogs
    bot.add_cog(MiscCommands(bot))  # instantiates MiscCommands Cog
