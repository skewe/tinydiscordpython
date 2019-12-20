@client.event
async def on_message(message):
    if message.content == ('hello snake'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello ','{.author}!'.format(msg))
