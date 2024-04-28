import discord
import base64

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)
token = 'YOUR TOKEN HERE'

def decode_7_times(encoded_text):
    decoded_text = encoded_text
    for _ in range(7):
        decoded_text = base64.b64decode(decoded_text).decode()
    return decoded_text

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    print(decode_7_times(f'{message.content}'))

client.run(token)