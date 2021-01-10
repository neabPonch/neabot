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

    @tasks.loop(hours=24)
    async def BTC_loop(self):
        message_channel = self.bot.get_channel(BOT_CRYPTO_CHANNEL)
        #print(f'Got channel {message_channel}')
        await Crypto.Crypto.BTC(self.bot, message_channel)

    @BTC_loop.before_loop
    async def before_BTC_loop(self):
        #print('waiting...')
        await self.bot.wait_until_ready()
        #print('Finished waiting')




def setup(bot):  # required for all Cogs
    bot.add_cog(Tasks(bot))  # instantiates Tasks Cog
