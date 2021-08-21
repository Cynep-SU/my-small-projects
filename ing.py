from __future__ import unicode_literals
import discord
import os
import pafy
client = discord.Client()
Play = False
played_list = []
x = 0
def x():
    return(x)
    X += 1

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_typing(message,a,b):
    if message.guild.voice_client is None or  message.guild.voice_client.is_playing() is not True:
        if len(played_list) > 0:
            result = pafy.new(played_list[x])
            x += 1
            if vc is None:
                vc = await channel.connect()
            source = discord.FFmpegPCMAudio(source = f"{result.title}" + '.webm', executable ='ffmpeg.exe' )
            vc.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
        else:
            await message.VoiceClient.dissconect()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        e = discord.Embed(title='Миша классный чел')
        await message.channel.send('Hello', embed=e)
        await message.channel.send(' ', file=discord.File('cool.jpg'))
        print(message.guild.voice_client)
    elif message.content.startswith('$list'):
        for i in played_list:
            result = pafy.new(played_list[x])
            await message.channel.send(f"{result.title}")
    elif message.content.startswith('$music'):
        print(message.guild)
        if message.guild.voice_client != None:
            played_list.append(message.content[7:])
        await message.channel.send('Трек добавлен в очередь')
        url = (message.content[7:])
        result = pafy.new(url)
        best_quality_audio = result.getbestaudio()
        print(best_quality_audio)
        try:
            best_quality_audio.download()
            print(f"{result.title}")
            channel = discord.utils.get(message.guild.voice_channels, name='Music')
            vc = await channel.connect()
            source = discord.FFmpegPCMAudio(source = f"{result.title}" + '.webm', executable ='ffmpeg.exe' )
            vc.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            print(discord.Guild.voice_client)
            print(vc)
        except:
            vc.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            await message.channel.send('Произошла неизвестная мне ошибка')

        #try:
           # vc.disconnect()
            #os.remove(f"{result.title}" + '.webm')
        #except:
            #Play = False
client.run('')
