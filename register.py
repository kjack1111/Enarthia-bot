import util
import latlong
import json

async def register(client, M):
    name = None
    leader = None
    government = None
    population = None
    capital = []
    resources = []
    human = M.author
    
    await client.send_message(M.channel, f"Hello, <@{human.id}>! It looks like you're trying to register a new nation! Please give me the Name.")
    rname = await client.wait_for_message(timeout=300, author=human, channel=M.channel)
    if rname==None:
        await util.timeout(client, M)
        return
    else:
        name = rname.content
        
    await client.send_message(M.channel, f"Thank you, <@{human.id}>! Can you please ping the user that you're registering the country for?")
    rleader = await client.wait_for_message(timeout=300, author=human, channel=M.channel)
    if rleader==None:
        await util.timeout(client, M)
        return
    else:
        leader = rleader.mentions[0].id
        
    await client.send_message(M.channel, f"Alright, <@{human.id}>. Please give me the Government type.")
    rgovt = await client.wait_for_message(timeout=300, author=human, channel=M.channel)
    if rgovt==None:
        await util.timeout(client, M)
        return
    else:
        govt = rgovt.content

    await client.send_message(M.channel, f"Thank you, <@{human.id}>. Please put in A NUMBER for the starting population.")
    rpopulation = await client.wait_for_message(timeout=300, author=human, channel=M.channel)
    if rpopulation==None:
        await util.timeout(client, M)
        return
    else:
        population = int(rpopulation.content)

    await client.send_message(M.channel, f"Can you please name the Capital City of the Nation <@{human.id}>? (If not applicable, a general location would be nice.) [THIS IS NOT THE FINAL VERSION, AND WILL LIKELY BE SWITCHED OUT FOR A GRADTULE QUESTIONARE]")
    rcapital = await client.wait_for_message(timeout=300, author=human, channel=M.channel)
    if rcapital==None:
        await util.timeout(client, M)
        return
    else:
        capital.append(rcapital.content)
        
    await client.send_message(M.channel, f"Finally, can you please outline the resources a nations has <@{human.id}>? (Resources are comma-seperated.")
    rresources = await client.wait_for_message(timeout=300, author=human, channel=M.channel)
    if rresources==None:
        await util.timeout(client, M)
        return
    else:
        sresources = rresources.content
        resources = {r.lower().strip():0 for r in sresources.split(",")}
        if ("astatine" in resources):
            await client.send_message(M.channel, "https://www.youtube.com/watch?v=gz3F-02FwZc")
            return

    initcountry = latlong.Country(leader, name, govt, population, resources, capital)
    print(initcountry)
    print(initcountry.__dict__)
    return initcountry
# await register.register(client, M)
