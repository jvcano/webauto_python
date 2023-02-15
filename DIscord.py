import discord
import config

class Myclient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    #async def on_message(self, message):
    #    print('Message from {0.author}: {0.content}'.format(message))
    #! this lines send you a reply after askign for command
    #async def on_message(self,message):
    #    prefix = ".help."
    #    if message.content.startswith(prefix):
    #        await message.channel.send("you need help?")
    async def on_message(self,message):
        prefix = ".help."
        if message.content.startswith(prefix):
            command = message.content[len(prefix):]
            await message.channel.send(f"the command is: {command}")
            await message.channel.send(f"the command is: {command}")

intents = discord.Intents.all()

client = Myclient(command_prefix='.',intents=intents)
#client.run(config.my_secret)

