import discord
from aibot import ask_vicky
discord_token = 
discord_name = 
discord_url = 
#Interface with discord. For the most part, this is the example from the discord module documentation, just with the added methods from aibot.
#If you need something more complex, they've got even more docs. 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print(message.content)
        response = ask_vicky(message.content)
        await message.channel.send(response)

client.run(discord_token)
