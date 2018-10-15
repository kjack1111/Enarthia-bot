import discord

async def listcountries(client, M, countries):
    client.send_typing(M.channel)
    for key, value in countries.items():
        em = discord.Embed(
            title=key,
            description=value["player"]
        )
        em.add_field(name="money", value=value["money"])
        em.add_field(name="iron", value=value["iron"])
        em.add_field(name="copper", value=value["copper"])
        await client.send_message(M.channel, "", embed=em)
    
