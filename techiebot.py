import discord
import asyncio as asyncio

from discord import Game, Embed
from discord.ext import commands

client = commands.Bot(command_prefix = '**')
TOKEN = 'TOKENSERIAL'

@client.event
async def on_ready():
    print('TechieBot Is Alive')

	
@client.command
async def startembed():
    if message.content.startswith("#start"):
        embed = discord.Embed(title="Java", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/4OQKynP.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="C", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/MjtPSLz.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="C#", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/iju4Jqi.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="C++", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/2ENDnXE.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="Perl", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/ss6T8Rb.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="Swift", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/OSgAELW.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="Python", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/toSFhCc.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="Lua", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/3A72Mjs.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="Ruby", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/tjSYyyH.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="ShellScript", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/RSm1fHv.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="HTML", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/Ho97box.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="CSS", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/1mbwQnC.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="JS", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/p0t29J4.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="PHP", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/KqJ1IA8.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="SQL", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/DkPS68o.png")
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(title="NodeJS", color=0x30A5D9)
        embed.set_author(name="Language", icon_url="https://cdn-images-1.medium.com/max/1600/1*CzwDS_yByKtMNdScO3RaPA.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/DDNnK1F.png")
        await client.send_message(message.channel, embed=embed)

		
@client.event
async def on_reaction_add(reaction, user):
    id = message.id
    javaid = 484525862310510592
    cid = 484525864269119519
    csid = 484525866177527819
    cppid = 484525868182405150
    perlid = 484525870174699520
    swiftid = 484525889002930176
    pythonid = 484525890911600648
    luaid = 484525893121998863
    rubyid = 484525895009304577
    shellscript = 484525896943009822
    htmlid = 484525911094460429
    cssid = 484525913476956180
    jsid = 484525915087437865
    phpid = 484525917448699919
    nodejsid = 484525938067898378
    if id == javaid:
        await user.addRole('Java')
    if id == cid:
        await user.addRole('C')
    if id == csid:
        await user.addRole('C#')
    if id == cppid:
        await user.addRole('C++')
    if id == perlid:
        await user.addRole('Perl')
    if id == swiftid:
        await user.addRole('Swift')
    if id == pyid:
        await user.addRole('Python')
    if id == luaid:
        await user.addRole('Lua')
    if id == rubyid:
        await user.addRole('Ruby')
    if id == shellscriptid:
        await user.addRole('ShellScript')
    if id == htmlid:
        await user.addRole('HTML')
    if id == cssid:
        await user.addRole('CSS')
    if id == jsid:
        await user.addRole('JS')
    if id == phpid:
        await user.addRole('PHP')
    if id == nodejsid:
        await user.addRole('NodeJS')

		
client.run(TOKEN)