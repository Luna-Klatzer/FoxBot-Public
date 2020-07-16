import sys, traceback
from threading import Timer
from discord.ext import tasks, commands
from datetime import datetime
from datetime import date

class Database_Setup(commands.Cog):
    def __init__(self, client):
        self.client = client
        now = datetime.now()
        date_now = date.today
        def ctime():
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return current_time
        current_time = ctime()
        print(f"{current_time} EXTENSION DATABASE RESPONDED")
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time}--DATABASE_SETUP LOGGED INTO FILE\n")


#Connecting with the main.py file
def setup(client):
    client.add_cog(Database_Setup(client))