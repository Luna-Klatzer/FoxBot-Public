import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
from datetime import datetime
from datetime import date
from discord.ext.commands import Bot
import sys, traceback
import random

now = datetime.now()
def ctime():
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time

class Members(commands.Cog):
    def __init__(self, client):
        self.client = client
        now = datetime.now()
        date_now = date.today
        current_time = ctime()
        print(f"{current_time} EXTENSION MEMBERS RESPONDED") 
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time}--MEMBERS LOGGED INTO FILE\n")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            #self.client works for the client attributes

            now = datetime.now()
            date_now = date.today
            current_time = ctime() # Defining the time again

            guild = self.client.get_guild(727228268696043583) # Getting the Guild
            role = discord.utils.get(guild.roles, name="Fox-Appreciator") # Searching for the Role in the guild
            if role is not None:
                await member.add_roles(role) # Adding a role to the new member

            print("Event on_member_join fired")
            now = datetime.now()
            date_now = date.today

            member_mention = f"<@{member.id}>"

            channel = self.client.get_channel(727240490319347822)
            print(f"---- CONSOLE ---- [{str(current_time)} {str(self.client.user)}] {member} has joined the server.")
            embed=discord.Embed(title="A new member joined the server!",color=0x00C09a)
            embed.set_thumbnail(url="https://i.imgur.com/AgZnWfk.jpg")
            embed.add_field(name=f"Welcome {member},", value=f"to the Fox-Appreciation Club!", inline=True)
            await channel.send(embed=embed)

            try:
                user = self.client.get_user(member.id)
                await user.send(f"Welcome to the 🦊Fox-Appreciation Club🦊,\n the fox council wishes you a nice stay and hopes that you enjoy your time on the server!😊👍")
            except Exception as e:
                now = datetime.now()
                date_now = date.today
                current_time = ctime()
                print(f"{current_time} ERROR IN SENDING THE MESSAGE TO THE USER:\n{str(e)}")
                with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
                    c.write(f"{current_time} --MEMBERS (sending message to user) {e}\n")

            try:
                for guild in self.client.guilds:
                    channel = self.client.get_channel(727232248671109210)
                    channel_name = f"🦊Fox Counter: {guild.member_count}🦊"
                    if channel_name == str(channel.name):
                        break
                    else:
                        await channel.edit(name=str(channel_name), reason="Membercounter is different!")

            except Exception as e:
                now = datetime.now()
                date_now = date.today
                current_time = ctime()
                print(f"{current_time} ERROR IN MEMBERS (on_member_join member counter update):\n{str(e)}")
                with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
                    c.write(f"{current_time} --MEMBERS (on_member_join member counter update) {e}\n")

        except Exception as e:
            now = datetime.now()
            date_now = date.today
            current_time = ctime()
            print(f"{current_time} ERROR IN MEMBERS:\n{str(e)}")
            with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
                c.write(f"{current_time} --MEMBERS {e}\n")

#Connecting with the main.py file
def setup(client):
    client.add_cog(Members(client))