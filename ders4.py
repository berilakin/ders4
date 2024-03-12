import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


import random
def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


import discord
from emoji import gen_emodji
from bot_mantik import gen_pass 
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith("/naber"):
        await message.channel.send("iyiyim sen nasılsın?")
    elif message.content.startswith('/bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("/pass"):
        await message.channel.send(gen_pass(15))    
    elif message.content.startswith("/emoji"):
        await message.channel.send(gen_emodji)       
    else:
        await message.channel.send(message.content)

client.run(".........")
