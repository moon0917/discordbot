import discord
import openpyxl
import requests
import asyncio
import os
from json import loads


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("국밥")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "moon09171769" 
    name = "rakki"
    channel = client.get_channel(792003618215690280)
    a = 0
    while True:
        headers = {'Client ID': 'f31uytrhb07pobsxbfy81yc6wze2xr'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a:0:
                await channel.send(name + "님이 방송중입니다'")
                a=1
        except:
            a = 0
        await asyncio.sleep(15)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
