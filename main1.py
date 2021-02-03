import discord
import openpyxl
import requests
import asyncio
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
client.run('546d7d9e9509ce6c62522b7fbdd7bf7f7aed6f39faa7bc778364a930ed78a66e')