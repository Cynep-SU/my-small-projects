import discord
from discord.ext import commands


TOKEN = ''
bot = commands.Bot(command_prefix='')


@bot.event
async def on_message(message: discord.Message):
    if "@everyone" in message.content:
        await message.guild.ban(message.author, reason="П использовал @everyone")


bot.run(TOKEN)
