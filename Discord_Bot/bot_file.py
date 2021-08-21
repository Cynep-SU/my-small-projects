import discord
from discord.ext import commands

# import threading

TOKEN = ''
bot = commands.Bot(command_prefix='!')
starting = False


# vc = ''


@bot.command()
async def work(ctx):
    if True:
        # starting = True
        channel = discord.utils.get(ctx.guild.voice_channels, name='Breath')
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='breath.mp3', executable='ffmpeg.exe')) # sound from https://youtu.be/SGF_iTLdw4U
        await ctx.send('Bot working')
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="мультики/cartoons"))



bot.run(TOKEN)
