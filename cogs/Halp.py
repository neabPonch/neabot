from discord.ext import commands

class Halp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='halp')
    async def halp(self, message):
        textwall = '''!random -> pants-shittingly awesome random neab quote
                   !quoteadd quotetext  -> adds quote (must be a neab to add)
                   !quotefind quotetext -> finds a quote containing text
                   !quote quotenumber -> call specific quote by number
                   !quotedelete quotenumber -> deletes quote by number (must be admin)
                   !BTC -> returns latest Bitcoin price
                   !gay -> gives accurate % of your gayness
                   !catjam -> cat jamming the fuck out
                   !athonking -> hmm
                   !gpt2 sometext -> uses shitty AI to complete the story
                   !play airhorn -> plays a random airhorn clip in voice
                   !play tf2 -> plays a random tf2 clip in voice
                   !play misc -> plays a random misc clip in voice           
                   '''
        await message.send(textwall)


def setup(bot):  # required for all Cogs
    bot.add_cog(Halp(bot))  # instantiates Halp Cog