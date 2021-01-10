import os
from dotenv import load_dotenv
from discord.ext import commands
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import datetime

load_dotenv()
CMC_KEY = os.getenv('CMC_KEY')

class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='BTC')
    @commands.has_role('neab')
    async def BTC(self, message):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '10',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': CMC_KEY,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            price = data['data'][0]['quote']['USD']['price']
            time = data['data'][0]['last_updated']
            newtime = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
            await message.send('The CoinMarketCap price of Bitcoin is ${0:,.2f} USD as of {1}'.format(price, newtime))
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

def setup(bot):
    bot.add_cog(Crypto(bot)) # instantiates Crypto cog