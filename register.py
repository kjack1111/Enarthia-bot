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
        
    await client.send_message(M.channel, f"Thank you, <@{human.id}>! Can you please ping the user that you're registering the country for?")
    rleader = await client.wait_for_message(timeout=15, author=human, channel=M.channel)
    if rleader==None:
        await util.timeout(client, M)
        return
    else:
        leader = rleader.mentions[0]
        
    await client.send_message(M.channel, f"Alright, <@{human.id}>. Please give me the Government type.")
    rgovt = await client.wait_for_message(timeout=15, author=human, channel=M.channel)
    if rgovt==None:
        await util.timeout(client, M)
        return
    else:
        govt = rgovt

    await client.send_message(M.channel, f"Thank you, <@{human.id}>. Please put in A NUMBER for the starting population.")
    rpopulation = await client.wait_for_message(timeout=15, author=human, channel=M.channel)
    if rpopulation==None:
        await util.timeout(client, M)
        return
    else:
        population = int(rpopulation)
        
        


# await register.register(client, M)
