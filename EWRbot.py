import discord
import json
import thekey
import register
import listcountries
import latlong
PREFIX = "$"
countries = []

with open("countries.json") as f:
    countries = [latlong.Country(**country) for country in json.load(f)]
    print(countries)

def savecountries():
    with open("countries.json", 'w') as f:
        json.dump(countries, f,
                  default=lambda o:o.__dict__
                  )

client = discord.Client()

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
        newcountry = await register.register(client, M)
        if(newcountry):
            countries.append(newcountry)
            savecountries()
    if(M.content.lower().startswith(PREFIX + "list")):
        print(countries)
        await listcountries.listcountries(client, M, countries)
            

@client.event
async def on_ready():
    print("Connected!")

client.run(thekey.token)
