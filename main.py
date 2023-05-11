"""
Sigma Bot v 1.0.0
Author : Cactochan
"""
from flask import Flask
import threading
import os
import openai
import logging
import re


msg = 'what will a sigma male  reply to the message "__q__"'
openai.api_key = os.environ['ai']
pattern = r'"([^"]*)"'

app = Flask(__name__)

@app.route('/')
def main_func_():
  print("PING__UPTIME")  
  return "Yes"

import discord
from discord.ext import commands

def get_reply(msg_this):
  rep = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": msg.replace("__q__", msg_this)},
    ]
  )
  rep = rep["choices"][0]['message']['content']

  print(rep)
  # e = len(msg_this.split(":")) - 1
  # rep = rep.split(":")[1 + e]
  try:
    try:
      x = re.findall(pattern, rep)[1]
      return x
    except:
      try:
        return re.findall(pattern, rep.split(":")[1])[0]
      except:
        return rep.split(":")[1]
  except:
    return "*Ignores you*"
  
  

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "~~~", intents=intents)

@client.event
async def on_ready():
    print("Started")

@client.event
async def on_message(message):
    if message.content.startswith("~~~"):
      await message.channel.send(get_reply(message.content[3:]))


my_secret = os.environ['token']

threading.Thread(target=client.run, 
                args=(my_secret,)).start()

import requests
import time
def recall():
  while True:
    time.sleep(6)
    requests.get("https://sigmabot.darkmash.repl.co")

# threading.Thread(target=recall).start()

app.run(host="0.0.0.0", port=8080)
