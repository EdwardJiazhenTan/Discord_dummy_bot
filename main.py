import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('token')
client.run('MTExMjQ3NDUzMTU3NjE2NDQxMg.GH9XYl.3RIaoMNRMH647WOR-s2jGJ-2mh3tOLUFOW8-9o')
