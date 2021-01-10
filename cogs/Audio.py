from discord.ext import commands
import asyncio
import discord
#import ffmpeg
import requests
from bs4 import BeautifulSoup
import random
import time


def getSoundLink(url):
    with requests.Session() as s:
        page = s.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    soundlist = []
    [soundlist.append(item) for item in list(soup.stripped_strings) if '.mp3' in item and item not in soundlist]
    soundclipurl = url + random.choice(soundlist)
    return soundclipurl


class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def play(self, message):
        user = message.message.author
        url = 'https://neabponch.com/soundclips/'+message.message.content[6:]+'/'
        try:
            soundurl = getSoundLink(url)
        except:
            await message.send('That didn\'t work...')
            return
        try:
            voice_channel = user.voice.channel
        except:
            await message.send('You need to be in a voice channel, dawg.')
            return
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source=soundurl), after=lambda e: print('done', e))
        while vc.is_playing():
            time.sleep(2)
        await vc.disconnect()
        await message.message.delete()


def setup(bot):  # required for all Cogs
    bot.add_cog(Audio(bot))  # instantiates Audio Cog