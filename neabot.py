# neabot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
BOT_TEST_CHANNEL = int(os.getenv('BOT_TEST_CHANNEL'))

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='!halp'))
    bot_channel = bot.get_channel(BOT_TEST_CHANNEL)
    await bot_channel.send('I am here.')


extensions = ['cogs.Listener',
              'cogs.Quotes',
              'cogs.Crypto',
              'cogs.MiscCommands',
              'cogs.GPT2',
              'cogs.Halp',
              'cogs.Audio',
              'cogs.Tasks',
              'cogs.Jokes']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run(TOKEN)
