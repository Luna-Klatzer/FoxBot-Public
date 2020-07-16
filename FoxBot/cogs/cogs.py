import sys, traceback
from threading import Timer
from discord.ext import tasks, commands
from datetime import datetime
from datetime import date
import typing
from typing import Optional
from FoxBot.main import *


class Cogs_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        now = datetime.now()
        date_now = date.today
        def ctime():
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return current_time
        current_time = ctime()
        print(f"{current_time} EXTENSION COGS_COMMANDS RESPONDED")
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time}--COGS_COMMANDS LOGGED INTO FILE\n")

@commands.has_role("-(Staff)-")
@commands.command()
async def cogs_list(self, ctx):
    now = datetime.now()
    date_now = date.today
    current_time = ctime() 
    i = None
    try:
        for filename in FoxBot.main.initial_extensions:
            if i == None:
                i = 1
                ctx.send("Extensions currently loaded: ")
            await ctx.send(f"{i}. {filename[:-3]},")
            i += 1
    except Exception as e:
        print(str(e))
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time} --COMMAND COGS_LIST{e}\n")  
        print(f"{current_time} COMMAND COGS_LIST FAILED!")
    
#Connecting with the main.py file
def setup(client):
    client.add_cog(Cogs_Commands(client))