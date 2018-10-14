async def register(client, M):
    human = M.author
    await client.send_message(M.channel, f"Hello, <@{human.id}>! It looks like you're trying to register a new nation! Please give me the Name.")
    M2 = await client.wait_for_message(timeout=30, author=human, channel=M.channel)
    if M2==None:
        await client.send_message(M.channel, "The command timed out! Please try again.")
    else:
        name = M2.content
        


# await register.register(client, M)
