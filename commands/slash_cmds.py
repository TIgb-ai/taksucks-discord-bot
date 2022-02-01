import nextcord
from nextcord import *
from nextcord.ext import commands
import random
from nextcord.ui import Button, View

test_guild = 893564988936040548 


class Slash_Cmds(commands.Cog):
    '''Slash Commands is availabe here'''

    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def 

    @nextcord.slash_command(name = 'ping',description = 'Sends all of the information about user',guild_ids=[test_guild])
    async def ping_(self,interac : Interaction):
        responses = [f'**Pong!** ```{round(self.bot.latency * 1000)}ms```',f'**Pong!** ```{round(self.bot.latency * 1000)}ms```']

        embed = nextcord.Embed(title="Pong!!")
        embed.set_footer(text = f'Ping = {round(self.bot.latency * 1000)} ms',icon_url="https://cdn.discordapp.com/avatars/938011170936332328/75cf5753a218804f9787f67a200d427a.png?size=1024")
    
        async def button_callback(interaction):
            emb = interaction.message.embeds[0].set_footer(text= f'Ping = {round(self.bot.latency * 1000)} ms',icon_url="https://cdn.discordapp.com/avatars/938011170936332328/75cf5753a218804f9787f67a200d427a.png?size=1024")
            await interaction.response.edit_message(embed=emb)

        button1 = Button(label='refresh', style=nextcord.ButtonStyle.grey , emoji= '🏓')
        view = View()
        button1.callback = button_callback
        view.add_item(button1)
        #await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')
        await interac.response.send_message(embed=embed,view=view)
        print(f'{interac.user.name} wants to know the ping of the bot!')   









def setup(bot):
    bot.add_cog(Slash_Cmds(bot))
    print('Slash Commands Ready!!!')
