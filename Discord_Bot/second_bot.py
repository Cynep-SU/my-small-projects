import json

import discord
from discord.ext import commands

# import threading

TOKEN = ''
bot = commands.Bot(command_prefix='!')
starting = False


# vc = ''


@bot.command(pass_context=True)
async def role_msg(ctx: discord.ext.commands.context.Context, *args):
    emoji_role = dict()
    x = 1
    print(args)
    for el in args:
        if x % 2 == 0:
            role = discord.utils.get(ctx.guild.roles, name=el)
            emoji_role[emoji] = role
            if x == len(args) - 1:
                break
        else:
            emoji = el
        x += 1
    channel = discord.utils.get(ctx.guild.text_channels, name=args[-1])
    print(emoji_role.items())
    msg = ''
    msg = await ctx.send(''.join([i + ' - ' + x.name + '\n' for i, x in emoji_role.items()]))
    for i in emoji_role.keys():
        emoji_role[i] = emoji_role[i].id
        await msg.add_reaction(i)
    try:
        with open("data.json", "r") as read_file:
            new_dict = json.load(read_file)
        new_dict[channel.id] = emoji_role
    except FileNotFoundError:
        new_dict = dict()
        new_dict[channel.id] = emoji_role
        with open("data.json", "w") as write_file:
            json.dump(new_dict, write_file)

    with open("data.json", "w") as write_file:
        json.dump(new_dict, write_file)


@bot.event
async def on_reaction_add(reaction, user):
    with open("data.json", "r") as read_file:
        new_dict = json.load(read_file)
    print(reaction, new_dict.keys())
    if str(reaction.message.channel.id) in new_dict.keys():
        role = discord.utils.get(user.server.roles, id=new_dict[reaction.message.channel.id][reaction.emoji])
        await bot.add_roles(user, role)

bot.run(TOKEN)
