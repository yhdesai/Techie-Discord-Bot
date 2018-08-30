import discord
import asyncio as asyncio

from discord import Game, Embed
from discord.ext import commands

client = commands.Bot(command_prefix = '**')
TOKEN = 'TOKENSERIAL'

@client.event
async def on_ready():
    print('TechieBot Is Alive')
		
		
@client.event
async def on_reaction_add(reaction, user):
    id = message.id
    javaid = 484525862310510592
    cid = 484525864269119519
    csharpid = 484525866177527819
    cppid = 484525868182405150
    perlid = 484525870174699520
    swiftid = 484525889002930176
    pythonid = 484525890911600648
    luaid = 484525893121998863
    rubyid = 484525895009304577
    shellscriptid = 484525896943009822
    htmlid = 484525911094460429
    cssid = 484525913476956180
    jsid = 484525915087437865
    phpid = 484525917448699919
    nodejsid = 484525938067898378
    if id == javaid:
        if reaction == java:
            await user.addRole('Java')
    if id == cid:
        if reaction == c:
            await user.addRole('C')
    if id == csharpid:
        if reaction == csharp:
            await user.addRole('C#')
    if id == cppid:
        if reaction == cpp:
            await user.addRole('C++')
    if id == perlid:
        if reaction == perl:
            await user.addRole('Perl')
    if id == swiftid:
        if reaction == swift:
            await user.addRole('Swift')
    if id == pythonid:
        if reaction == python:
            await user.addRole('Python')
    if id == luaid:
        if reaction == lua:
            await user.addRole('Lua')
    if id == rubyid:
        if reaction == ruby:
            await user.addRole('Ruby')
    if id == shellscriptid:
        if reaction == shellscript:
            await user.addRole('ShellScript')
    if id == htmlid:
        if reaction == html:
            await user.addRole('HTML')
    if id == cssid:
        if reaction == css:
            await user.addRole('CSS')
    if id == jsid:
        if reaction == js:
            await user.addRole('JS')
    if id == phpid:
        if reaction == php:
            await user.addRole('PHP')
    if id == nodejsid:
        if reaction == nodejs:
            await user.addRole('NodeJS')

		
client.run(TOKEN)
