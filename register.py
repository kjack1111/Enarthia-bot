import util

async def register(client, M):
    human = M.author
    await client.send_message(M.channel, f"Hello, <@{human.id}>! It looks like you're trying to register a new nation! Please give me the Name.")
    rname = await client.wait_for_message(timeout=15, author=human, channel=M.channel)
    if rname==None:
        await util.timeout(client, M)
        return
    else:
        name = rname
    await client.send_message(M.channel, f"Alright, <@{human.id}>. Please give me the Government type.")
    rgovt = await client.wait_for_message(timeout=15, author=human, channel=M.channel)
    if rgovt==None:
        await util.timeout(client, M)
        return
    else:
        govt = rgovt
        


# await register.register(client, M)
