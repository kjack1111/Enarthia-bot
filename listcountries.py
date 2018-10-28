import discord

async def listcountries(client, M, countries):
    client.send_typing(M.channel)
    for current in countries:
        em = discord.Embed(
            title=current.name,
            description=current.leader
        )
        c = current
        for res, amt in current.resources.items():
            em.add_field(name=res, value=amt)
        await client.send_message(M.channel, "", embed=em)
    
