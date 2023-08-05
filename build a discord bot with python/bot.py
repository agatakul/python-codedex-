#!/usr/bin/env python3

import discord
import requests
import json
from dotenv import dotenv_values


#requests package allows us to make HTTP requests to any URL. In this case we're calling the GET method to the URL that will give us the meme data

#json package allows us to read JSON data. This is useful since most data passed around on the web is in the JSON format, like the JSON response we saw above
config = dotenv_values(".env")
token = config['TOKEN']

def get_meme():
	response = requests.get('https://meme-api.com/gimme')
	json_data = json.loads(response.text)
	return json_data['url']


class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as{0}!'.format(self.user))
		
	# Responding to Messages
	async def on_message(self, message):
		if message.author == self.user:
			return
		
		if message.content.startswith('$meme'):
			await message.channel.send(get_meme())
		
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token) 

# That's all it takes to set up and code a Discord bot in Python! Just a note: the bot will respond to you as long as the program is kept running. If you close your terminal or turn off your computer, it will no longer be running. If you want to keep the program running forever, we’ll have to deploy it to another computer in the cloud. However, that is a lesson for another day.
#
		
