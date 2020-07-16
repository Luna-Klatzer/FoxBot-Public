import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
from datetime import datetime
from datetime import date
from discord.ext.commands import Bot
import sys, traceback
from threading import Timer
from discord.ext import tasks, commands
import random

class Time(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.index_time_update.start()
        #self.index_verification.start()
        self.index_seconds = 0
        now = datetime.now()
        date_now = date.today
        def ctime():
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return current_time
        current_time = ctime()
        print(f"{current_time} EXTENSION TIME RESPONDED")
        #self.index_verification.add_exception_type(asyncpg.PostgresConnectionError)
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time}--BACKGROUDN_TASK LOGGED INTO FILE\n")

    def cog_unload(self):
        self.index_time_update.cancel()
        #self.index_verification.cancel()

    @tasks.loop(seconds=1.0)
    async def index_time_update(self):
        now = datetime.now()
        date_now = date.today
        def ctime():
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return current_time
        current_time = ctime()
        try:
            self.index_seconds += 1       

            for guild in self.client.guilds:
                channel = self.client.get_channel(727232248671109210)
                channel_name = f"🦊Fox Counter: {guild.member_count}🦊"
                if channel_name == str(channel.name):
                    break
                else:
                    try:
                        await channel.edit(name=str(channel_name), reason="Membercounter is different!")
                    except Exception as e:
                        now = datetime.now()
                        date_now = date.today
                        current_time = ctime()
                        print(f"{current_time} ERROR IN BACKGROUND_TASK (member counter update):\n{str(e)}")
                        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
                            c.write(f"{current_time} --MEMBERS (member counter update) {e}\n")

        except Exception as e:
            self.index_minutes = int(self.index_seconds/60)
            self.index_hours = int(self.index_minutes/60)
            print(f"ERROR IN BACKGROUND_TASK AFTER {self.index_seconds} seconds/{self.index_minutes} minutes/{self.index_hours} hours:\n{str(e)}")
            with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
                c.write(f"{current_time} --BACKGROUDN_TASK FAILED AFTER {self.index} seconds: {e}\n")

#Connecting with the main.py file
def setup(client):
    client.add_cog(Time(client))