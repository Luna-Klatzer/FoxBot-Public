import sys, traceback
from threading import Timer
from discord.ext import tasks, commands
from datetime import datetime
from datetime import date
import discord

class On_Message(commands.Cog):
    def __init__(self, client):
        self.client = client
        now = datetime.now()
        date_now = date.today
        def ctime():
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return current_time
        current_time = ctime()
        print(f"{current_time} EXTENSION ON_MESSAGE RESPONDED")
        with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
            c.write(f"{current_time}--ON_MESSAGE LOGGED INTO FILE\n")  
        command_prefix = "."
   
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            await self.client.wait_until_ready()
            now = datetime.now()
            date_now = date.today
            def ctime():
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                return current_time
            current_time = ctime()
            #author.mention
            author_id = f"<@{message.author.id}>"#discord-author_id
            if message.author == self.client.user:
                return
                await self.client.process_commands(message)
            elif message.guild is not None:
                if message.content == "prefix" !=-1:
                    return
                else:
                    user_id = message.author
                    if len(message.content) == 0 or len(message.content) < 1:
                        await self.client.process_commands(message)
                        return
                    else:
                        #Printing the message into the console with coloring, time and chat-information. 
                        if message.guild == None: 
                            print(f"{str(current_time)} {str(self.client.user)} {str(user_id)} wrote in '{str(message.channel)}': {str(message.content)}")
                            with open('./FoxBot/data/console.txt', 'a+') as c:
                                c.write(f"---- CONSOLE ---- [{str(current_time)} {str(self.client.user)}] {str(user_id)} wrote in '{str(message.channel)}': {str(message.content)}\n")
                        print(f"{str(current_time)} {str(self.client.user)} {str(user_id)} wrote in '{str(message.channel)}' on {message.guild}: {str(message.content)}")
                        with open('./FoxBot/data/console.txt', 'a+') as c:
                            c.write(f"---- CONSOLE ---- [{str(current_time)} {str(self.client.user)}] {str(user_id)} wrote in '{str(message.channel)}' on {message.guild}: {str(message.content)}\n")    
                        await self.client.process_commands(message)
            else:
                user_id = message.author
                guild = self.client.get_guild(727228268696043583)
                if message.content != None:
                    await user.send(f"{author_id} Is there something you need? Well in case you need help: Just contact the server staff. They will be very glad to help you. 👍")

                user = self.client.get_user(message.author.id)
                if message.guild == None: 
                    print(f"{str(current_time)} {str(self.client.user)} {str(user_id)} {str(user_id)} wrote in '{str(message.channel)}': {str(message.content)}")
                    with open('./FoxBot/data/console.txt', 'a+') as c:
                        c.write(f"---- CONSOLE ---- [{str(current_time)} {str(self.client.user)}] {str(user_id)} wrote in '{str(message.channel)}': {str(message.content)}\n")
                    await self.client.process_commands(message)

        except Exception as e:
            print(str(e))
            ErrorMessage = str(e)
            with open('./FoxBot/data/error_cache_cog_tasks.txt', 'a+') as c:
                c.write(f"{current_time} --ON_MESSAGE {e}\n")  
            if ErrorMessage.startswith("'charmap' codec can't encode character"):
                print(f"{current_time} -WARNING- On_message EVENT FAILED BECAUSE BOT WAS UNABLE TO ENCODE THE MESSAGE!")
            else:
                print(f"{current_time} On_message EVENT FAILED!")

#Connecting to the main.py file
def setup(client):
    client.add_cog(On_Message(client))