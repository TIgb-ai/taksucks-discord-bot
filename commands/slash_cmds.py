import nextcord
from nextcord import *
from nextcord.ext import commands
import random
from nextcord.ui import Button, View
from datetime import datetime
from utils.suggest import votelol



suggestembedcolour = 0xEB3636








class Slash_Cmds(commands.Cog):
    '''Slash Commands is availabe here'''

    def __init__(self, bot):
        self.bot=bot
        
        
        
        
        

    @commands.Cog.listener()
    async def on_member_join(self,member):
        general_welcome_channel = self.bot.get_channel(906429210954964994)
        await general_welcome_channel.send(f"Guys {member.mention} Just Joined Server Welcome them!!! <:swaghaiapna:928908517023289424>")
        
        
        
        

    @nextcord.slash_command(name = 'ping',description = 'Sends all of the information about user')
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




    @nextcord.slash_command(name = 'suggest',description='Suggest some things to staff')
    async def suggest_a(self,interac : Interaction,suggestion):
        em= nextcord.Embed(title=f"Suggested by {interac.user}",description=f"`{suggestion}`",color=suggestembedcolour,timestamp= datetime.now())
        em.set_thumbnail(url=f"{interac.user.avatar}")
        em.set_footer(text = f"id = {interac.user.id} ",icon_url="https://images-ext-2.discordapp.net/external/UkmH-vgKvt5rHVzldVKYdqUu9Pi1hIuoDdSwevaiD20/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/932339746275991622/a84cb436ee2844fb879fc27e637a23a7.png")
        suggestions_channel = self.bot.get_channel(938147776628420689)
        await suggestions_channel.send(embed=em,view=votelol())
        await interac.response.send_message("Thank Your Your suggestion is successfully sent to <#938147776628420689>" ,ephemeral=True)





def setup(bot):
    bot.add_cog(Slash_Cmds(bot))
    print('Slash Commands Ready!!!')
