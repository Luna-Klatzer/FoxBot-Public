import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
from datetime import datetime
from datetime import date
from discord.ext.commands import Bot
import sys, traceback


class On_raw_reaction_add(commands.Cog):
    def __init__(self, client):
        command_prefix = "st!"
        client = commands.Bot(command_prefix = command_prefix, description='A bot projekt for SWCD')
        self.client = client
        now = datetime.now()
        date_now = date.today
        def ctime():
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return current_time
        current_time = ctime()
        print(f"{current_time} EXTENSION ON_RAW_REACTION_ADD RESPONDED")
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time}--ON_RAW_REACTION_ADD LOGGED INTO FILE\n")


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        try:
            now = datetime.now()
            date_now = date.today
            def ctime():
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                return current_time
            current_time = ctime()
            message_id = payload.message_id

        except Exception as e:
            now = datetime.now()
            def ctime():
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                return current_time
            current_time = ctime()
            date_now = date.today
            print(f"{current_time} ERROR IN VERIFICATION:\n{str(e)}")
            with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
                c.write(f"{current_time} --On_raw_reaction_add {e}\n")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test Successful!")

#Connecting with the main.py file
def setup(client):
    client.add_cog(On_raw_reaction_add(client))