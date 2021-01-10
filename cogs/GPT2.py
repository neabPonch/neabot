import os
from dotenv import load_dotenv
from discord.ext import commands
import requests

load_dotenv()
GPT2_API_KEY = os.getenv('GPT2_API_KEY')

class GPT2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gpt2')
    async def gpt2(self, message):
        gpttextrequest = message.message.content[6:]
        await message.send('This is going to take a few seconds...')
        r = requests.post(
            "https://api.deepai.org/api/text-generator",
            data={
                'text': gpttextrequest,
            },
            headers={'api-key': GPT2_API_KEY}
        )
        await message.send(r.json()['output'][:500])


def setup(bot):  # required for all Cogs
    bot.add_cog(GPT2(bot))  # instantiates GPT2 Cog