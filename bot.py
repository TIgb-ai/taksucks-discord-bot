import os
import nextcord
import logging
from dotenv import load_dotenv
from nextcord.ext import commands
import os
import json
import logging
import datetime
import asyncio


# Third party libraries
import nextcord
from pathlib import Path
from nextcord.ext import commands

# Local code


class Tutorial(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # Greetings
    @commands.Cog.listener()
    async def on_ready(self):
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name='=help'))
       
        print(f'Logged in as {self.bot.user} ({self.bot.user.id})')
        

    # Reconnect
    @commands.Cog.listener()
    async def on_resumed(self):
        print('Bot has reconnected!')

    # Error Handlers
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Uncomment line 26 for printing debug
        # await ctx.send(error)

        # Unknown command
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid Command!')

        # Bot does not have permission
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('Bot Permission Missing!')



# Gateway intents
intents = nextcord.Intents.default()
intents.members = True
intents.presences = True

# Bot prefix

bot = commands.Bot(command_prefix=commands.when_mentioned_or('='),
                   description='Taksucks Bot', intents=intents)


# Logging
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Loading data from .env file
load_dotenv()
token = os.getenv('TOKEN')





if __name__ == '__main__':
    # Load extension
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[: -3]}')

    bot.add_cog(Tutorial(bot))
    bot.run(token, reconnect=True)