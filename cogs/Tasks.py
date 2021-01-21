from discord.ext import commands, tasks
import asyncio
import datetime as dt
import os
from dotenv import load_dotenv
import cogs.Crypto as Crypto

load_dotenv()
BOT_CRYPTO_CHANNEL = int(os.getenv('BOT_CRYPTO_CHANNEL'))

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.BTC_loop.start()

    @tasks.loop(minutes=30)
    async def BTC_loop(self):
        #print('made it to Tasks BTC_loop')
        message_channel = self.bot.get_channel(BOT_CRYPTO_CHANNEL)
        #print('made it to Tasks message_channel')
        price, newtime = Crypto.Crypto.getprice(self)
        #print('made it to Tasks price, newtime')
        await message_channel.edit(topic='BTC ${0:,.2f} @ {1}'.format(price, newtime))
        #print('made it to message_channel.edit...')


    @BTC_loop.before_loop
    async def before_BTC_loop(self):
        #print('waiting...')
        await self.bot.wait_until_ready()
        #print('Finished waiting')


def setup(bot):  # required for all Cogs
    bot.add_cog(Tasks(bot))  # instantiates Tasks Cog
