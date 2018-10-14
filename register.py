async def register(client, M):
        await client.send_message(M.channel, f"Hello, <@{M.author.id}>! It looks like you're trying to register a new nation! Please give me the Name.")
        M2 = await client.wait_for_message(timeout=30, author=M.author, channel=M.channel)
        name = M2.content
        print(name)


# await register.register(client, M)
