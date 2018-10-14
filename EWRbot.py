import discord
import thekey

client = discord.Client()

@client.event
async def on_message(M):
    if(M.content == "!hello"):
       await client.send_message(M.channel, "Hi!")
    if(M.content == "!HCF"):
        if(M.author.id == "113355491450613760"):
            await client.send_message(M.channel, "Burning Microprocessor!")
            await client.logout()
            raise SystemExit

@client.event
async def on_ready():
    print("Connected!")

client.run(thekey.token)
