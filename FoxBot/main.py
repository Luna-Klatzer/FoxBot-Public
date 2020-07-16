import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from datetime import datetime
from datetime import date
from typing import Optional
from discord.ext.commands import Bot
import sys, traceback
import os
from threading import Timer
from discord.ext import tasks, commands
import json

try:
    date_now = date.today
    def ctime():
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return current_time
    current_time = ctime()

    TOKEN = 'ENTER_TOKEN'

    command_prefix = "."
    client = commands.Bot(command_prefix = command_prefix, description='A bot projekt for SWCD')
    initial_extensions = ['members.py',
                        'cogs.py',
                        'on_message.py',
                        'startup.py',
                        'background.py',
                        'setup.py',
                        'database.py',
                        'on_raw_reaction_add.py'] 

except Exception as e:
    date_now = date.today
    current_time = ctime()
    print(f"{current_time} --MAIN FILE FAILED TO START DUE TO ERROR: {e}")
    with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
        c.write(f"{current_time} MAIN FILE FAILED TO START DUE TO ERROR: {e}\n") 

client.remove_command('help')

for filename in os.listdir('FoxBot/cogs'):
    date_now = date.today
    current_time = ctime()
    if filename == "__init__.py":
        break
    elif filename.endswith('.py') and filename in initial_extensions:
        client.load_extension(f'FoxBot.cogs.{filename[:-3]}')
        print(f"{current_time} EXTENSION {filename} LOADED!")              
 
@commands.has_role("-(Staff)-")
@client.command()
async def unload(ctx, extension: Optional[str] = None):
    current_time = ctime()
    now = datetime.now()
    def ctime():
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return current_time
    current_time = ctime()
    try:
        if extension == None:
            for filename in initial_extensions:
                if filename.endswith('.py'):
                    client.unload_extensions(f'cogs.{extension}')
                else:
                    client.unload_extension(f'cogs.{extension}')
        else:
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{extension[:-3]}')
            else:
                client.unload_extension(f'cogs.{extension}')

    except Exception as e:
        print(str(e))
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time} --COMMAND RELOAD {e}\n")  
        print(f"{current_time} COMMAND RELOAD FAILED!")

@commands.has_role("Intern-Fox")
@client.command()
async def reload(ctx, extension: Optional[str] = None):
    now = datetime.now()
    date_now = date.today
    def ctime():
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return current_time
    current_time = ctime()
    try:
        if extension == None:
            for filename in initial_extensions:
                if filename.endswith('.py'):
                    client.unload_extension(f'cogs.{extension[:-3]}')
                    client.load_extension(f'cogs.{extension[:-3]}')
                else: 
                    client.unload_extension(f'cogs.{extension}')
                    client.load_extension(f'cogs.{extension}')
        else:
            if extension.endswith('.py'):
                client.unload_extension(f'cogs.{extension[:-3]}')
                client.load_extension(f'cogs.{extension[:-3]}')
            else:
                client.unload_extension(f'cogs.{extension}')
                client.load_extension(f'cogs.{extension}')

    except Exception as e:
        print(str(e))
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time} --COMMAND UNLOAD {e}\n")  
        print(f"{current_time} COMMAND UNLOAD FAILED!")



@client.event
async def on_ready():
    try:
        now = datetime.now()
        date_now = date.today
        def ctime():
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return current_time
        current_time = ctime()
        filename = "background.py"
        background_task = client.get_cog('background')
        if background_task != None:
            client.unload_extension(f'{filename[:-3]}')
        client.load_extension(f'{filename[:-3]}')

    except Exception as e: 

        ErrorMessage = str(e) 
        if ErrorMessage == "Extension 'background' could not be loaded.":
            print(f"{current_time} -WARNING- Second Loading of Background Task failed because it's already loaded!")
        else:
            print(f'{current_time} Second Loading of Background Task failed because of: {e}!')

    try:
        now = datetime.now()
        date_now = date.today
        def ctime():
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return current_time
        current_time = ctime()

        with open('./FoxBot/data/console.txt', 'a+') as c:
            c.write(f"---- CONSOLE ---- [{str(current_time)} {str(client.user)}] Starting from TOKEN...\n")

        activity = discord.Activity(name='Fox Videos', type=discord.ActivityType.watching)   
        await client.change_presence(activity=activity)


        print(f'{current_time} Starting Client from TOKEN!')
        await asyncio.sleep(.150)

        i = 0
        while i < 3:
            await asyncio.sleep(1)
            print(f"{current_time} .")
            i = i+1

        print(f'{current_time} Logged in as {client.user.name}')
        print(f'{current_time} With ID {client.user.id}')
        print(f'{current_time} Server Counter:')

        for guild in client.guilds:
            print(f"{current_time} -{guild.name}(ID={guild.id})")

        print(f'{current_time} CONSOLE BOOTING...')

        i = 0
        while i < 5:
            await asyncio.sleep(.500)
            print(f"{current_time} .")
            i = i+1

        print(f'{current_time} CONSOLE BOOTED SUCCESSFULLY')
        
        with open('./FoxBot/data/console.txt', 'a+') as c:
            c.write(f"---- CONSOLE ---- [{str(current_time)} {str(client.user)}] Bot started successfully!\n")

    except Exception as e:
        print(str(e))
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time} --CONSOLE BOOT FAILED DUE {e}\n")
        print("{current_time} CONSOLE BOOT FAILED DUE TO CRITICAL ERROR!")

client.run(TOKEN, bot=True, reconnect=True)
