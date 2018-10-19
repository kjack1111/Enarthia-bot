import discord
import json
import thekey
import register
import listcountries
PREFIX = "$"
countries = {}

client = discord.Client()
with open("countries.json") as f:
    countries = json.load(f)

@client.event
async def on_message(M):
    if(M.content.lower().startswith(PREFIX + "help")):
       await client.send_message(M.channel, "``$Register: Registers your nation.``")
    if(M.content.lower().startswith(PREFIX + "hcf")):
        if(M.author.id == "113355491450613760"):
            await client.send_message(M.channel, "Burning Microprocessor!")
            await client.logout()
            raise SystemExit
    if(M.content.lower().startswith(PREFIX + "register")):
        await register.register(client, M)
    if(M.content.lower().startswith(PREFIX + "list")):
        await listcountries.listcountries(client, M, countries)
            

@client.event
async def on_ready():
    print("Connected!")

client.run(thekey.token)

import latlong.py
