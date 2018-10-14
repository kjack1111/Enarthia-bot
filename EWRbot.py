import discord
import thekey
import register
PREFIX = "$"

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
        await register.register(client, M)

@client.event
async def on_ready():
    print("Connected!")

client.run(thekey.token)
