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
