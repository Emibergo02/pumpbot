import discord

channel_id = 836973779514949688
token= "OTEzMzM4ODA0OTg1ODEwOTk0.YZ9EWQ.Y9Ghqv-YkGSZqNtEqIg3s1x36pU"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.channel.id != channel_id:
            return

        if message.content == 'hei':
            await message.channel.send('hei')

def startDiscord():
    client = MyClient()
    client.run(token)