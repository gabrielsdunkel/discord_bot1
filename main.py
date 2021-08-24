import discord
import os
import requests
import json
import random

client = discord.Client()

orlando_words = ["Sexo", "sexo"]

orlando_esquisito = [
  "Todo esquisito...",
  "Somente sexta-feiras após as 18:00",
  "Tu só fala disso"
  ]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0] ['q'] + " -" + json_data[0] ['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith('c!inspire'):
    quote = get_quote()

    await message.channel.send(quote)
  if msg.startswith('Tino'):
    await message.channel.send('é gay')
  if msg.startswith('tino'):
    await message.channel.send('é gay')

  if any(word in msg for word in orlando_words):
    await message.channel.send(random.choice(orlando_esquisito))


client.run(os.environ['TOKEN'])
