import nextcord
from nextcord import *
from nextcord.ext import commands
import random
from nextcord.ui import Button, View
from datetime import datetime
import json
import time




class Slash_Cmds_2(commands.Cog):
    '''Slash Commands is availabe here'''


    def __init__(self, bot):
        self.bot=bot
        
        
    async def update_data(self, afk, user):
        if not f'{user.id}' in afk:
            afk[f'{user.id}'] = {}
            afk[f'{user.id}']['AFK'] = 'False'
            afk[f'{user.id}']['reason'] = 'None'
    
    async def time_formatter(self, seconds: float):
        '''
        Convert UNIX time to human readable time.
        '''
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        tmp = ((str(days) + "d, ") if days else "") + \
            ((str(hours) + "h, ") if hours else "") + \
            ((str(minutes) + "m, ") if minutes else "") + \
            ((str(seconds) + "s, ") if seconds else "")
        return tmp[:-2]
    
    @commands.Cog.listener()
    async def on_message(self, message):
        with open('db/afk.json', 'r') as f:
            afk = json.load(f)
        
        for user_mention in message.mentions:
            if afk[f'{user_mention.id}']['AFK'] == 'True':
                if message.author.bot: 
                    return
                
                reason = afk[f'{user_mention.id}']['reason']
                meth = int(time.time()) - int(afk[f'{user_mention.id}']['time'])
                been_afk_for = await self.time_formatter(meth)
                embed = nextcord.Embed(description=f'{user_mention.name} Is currently AFK!\nReason : {reason}')
                await message.channel.send(content=message.author.mention, embed=embed)
                
                meeeth = int(afk[f'{user_mention.id}']['mentions']) + 1
                afk[f'{user_mention.id}']['mentions'] = meeeth
                with open('db/afk.json', 'w') as f:
                    json.dump(afk, f)
        
        if not message.author.bot:
            await self.update_data(afk, message.author)

            if afk[f'{message.author.id}']['AFK'] == 'True':
                
                meth = int(time.time()) - int(afk[f'{message.author.id}']['time'])
                been_afk_for = await self.time_formatter(meth)
                mentionz = afk[f'{message.author.id}']['mentions']

                embed = nextcord.Embed(description=f'Welcome Back {message.author.name}!', color=0x00ff00)
                embed.add_field(name="You've been AFK for :", value=been_afk_for, inline=False)
                embed.add_field(name='Times you got mentioned while you were afk :', value=mentionz, inline=False)

                await message.channel.send(content=message.author.mention, embed=embed)
                
                afk[f'{message.author.id}']['AFK'] = 'False'
                afk[f'{message.author.id}']['reason'] = 'None'
                afk[f'{message.author.id}']['time'] = '0'
                afk[f'{message.author.id}']['mentions'] = 0
                
                with open('db/afk.json', 'w') as f:
                    json.dump(afk, f)
                
                try:
                    await message.author.edit(nick=f'{message.author.display_name[5:]}')
                except:
                    print(f'I wasnt able to edit [{message.author}].')
        
        with open('afk.json', 'w') as f:
            json.dump(afk, f)
        

        
    @nextcord.slash_command(name = 'afk',description='Set Your AFK to let others know when they ping you')
    async def afk_a(self,interac : Interaction,reason):
        with open('db/afk.json', 'r') as f:
            afk = json.load(f)

        if not reason:
            reason = 'None'
        
        await self.update_data(afk, interac.user)
        afk[f'{interac.user.id}']['AFK'] = 'True'
        afk[f'{interac.user.id}']['reason'] = f'{reason}'
        afk[f'{interac.user.id}']['time'] = int(time.time())
        afk[f'{interac.user.id}']['mentions'] = 0

        embed = nextcord.Embed(description=f"I've set your AFK {interac.user.display_name}!\nReason : {reason}", color=0x00ff00)
        await interac.response.send_message(content=interac.user.mention, embed=embed)

        with open('db/afk.json', 'w') as f:
            json.dump(afk, f)
        try:
            await interac.user.edit(nick=f'[AFK]{interac.user.display_name}')
        except:
            print(f'I wasnt able to edit [{interac.user}].')        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def setup(bot):
    bot.add_cog(Slash_Cmds_2(bot))
    print('Slash Commands 2 Ready!!!')
