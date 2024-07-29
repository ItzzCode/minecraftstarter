import discord

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

    if message.content.startswith('<start'):
        await message.channel.send('Hello!')

secret_file = open("secret", "r")
secret = secret_file.read()
secret_file.close()
client.run(secret)