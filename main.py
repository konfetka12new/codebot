import discord
import asyncio
import colorama
import json
import random
import os
import requests
import replit
import ctypes
import sys
import time
from discord.ext import commands
from discord import Permissions
from discord import Webhook
from colorama import Fore
from discord.utils import get
from threading import Thread
from itertools import cycle
import datetime
from datetime import datetime
import fade
from discord.utils import utcnow
from datetime import timedelta
from discord.ext.commands import check
import re
import datetime

TOKEN = 'MTI0ODUyMTQ4NTkxNjU2OTY2MA.Gg41mL.K5q8AX5KWbRL1mlnmHWps7zD9xTFfsYm9AhDaM'

guild_ids = [1237788694245675170]

client = commands.Bot(command_prefix="!", intents=discord.Intents.all(), guild_ids=guild_ids)

log_channel_id = 1249332294414630993

@client.event
async def on_guild_join(guild):
    if guild.id not in guild_ids:
        await guild.leave()

@client.event
async def on_message(message):
    if message.guild.id not in guild_ids:
        return

    if message.author.bot:
        return

    # Check if the user has the specified roles
    if any(role.id in [1237788694333882395, 1237788694346469377, 1237788694346469382] for role in message.author.roles):
        return

    if "<@645149664911425557>" in message.content.lower():
        await message.delete()
        response_message = await message.channel.send(f"<@{message.author.id}>, Нельзя пинговать девелоперов!!!", mention_author=False)
        await asyncio.sleep(2)
        await response_message.delete()

    if "!скачать" in message.content.lower():
        response = message.content.lower().replace("!скачать", f"Скачать чит можно в канале: <#{1237788694631550984}>. Подробный гайд: https://www.youtube.com/watch?v=nIL4DQN7RE8")
        await message.channel.send(response, reference=message)

    if "!кфг" in message.content.lower():
        response = message.content.lower().replace("!кфг", f"Скачать пак кфг можно в канале <#{1249254741670887444}>.")
        await message.channel.send(response, reference=message)

    if "!рейсер" in message.content.lower():
        response = message.content.lower().replace("!рейсер", f"https://cdn.discordapp.com/attachments/1237788694791061556/1249404704786485258/photo_2024-06-09_21-41-10.gif?ex=66672e4e&is=6665dcce&hm=8c357633fedeae8837b144aed0405af05d462dfe3a7e34d394e1ddc3f1db6bed&")
        await message.channel.send(response, reference=message)  

    if "discord.gg" in message.content.lower():
        await message.delete()
        await message.author.ban(reason="Advertising")

        log_channel = client.get_channel(log_channel_id)
        ban_message = f"{message.author.mention} был забанен за рекламу. Точное время: {datetime.datetime.now(datetime.UTC)}"
        await log_channel.send(ban_message)

        ban_info_message = f"Пользователь {message.author.mention} был забанен за рекламу в канале {log_channel.mention}. Точное время: {datetime.datetime.now(datetime.UTC)}"
        await message.channel.send(ban_info_message)

    if "!помощь" in message.content.lower():
        commands_list = [
            "**!скачать - гайд как скачать чит**",
            "**!кфг - канал с пак кфг фри**",
            "**!рейсер - фоточка кринжа**",
        ]

        embed = discord.Embed(color=discord.Color.dark_theme())
        embed.set_author(name="Помощь", icon_url=message.guild.icon.url)
        embed.description = "Все действующие команды бота:"

        for command in commands_list:
            embed.add_field(name=command, value="\u200b", inline=False)

        embed.set_thumbnail(url=message.guild.icon.url)

        response_message = await message.channel.send(embed=embed)
        await response_message.edit(content=None, embed=embed)

    if "!сервачок" in message.content.lower():
        guild = message.guild
        online_members = len([member for member in guild.members if member.status!= discord.Status.offline])
        total_members = len(guild.members)
        embed = discord.Embed(color=discord.Color.dark_theme())
        embed.set_thumbnail(url=guild.icon.url)
        embed.description = f"Информация о сервере:\n"
        embed.description += f"Название сервера: **{guild.name}**\n"
        embed.description += f"Владелец сервера: **{guild.owner.mention}**\n"
        embed.description += f"Количество участников: **{total_members}**\n"
        embed.description += f"Онлайн участников: **{online_members}**\n"
        response_message = await message.channel.send(embed=embed)

@client.command()
async def ping(ctx):
    start_time = time.time()
    message = await ctx.send("Pinging...")
    end_time = time.time()
    latency = (end_time - start_time) * 1000
    await message.edit(content=f"Pong! Latency: {latency:.2f}ms")


        
client.run(TOKEN)   