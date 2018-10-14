async def timeout(client, M):
    await client.send_message(M.channel, "The command timed out! Please try again.")
