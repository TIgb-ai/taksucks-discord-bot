import nextcord
from nextcord import *
from nextcord.ui import Button, View



class votelol(nextcord.ui.View):
    def __init__(self):
        
        
        super().__init__(timeout=None)
        self.already_voted = []



    @nextcord.ui.button(label='0', style=nextcord.ButtonStyle.green,emoji="👍🏼")
    async def count(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        number = int(button.label) if button.label else 0
        
        if number + 1 >= 1:
            button.style = nextcord.ButtonStyle.green
            button.disabled = False
        button.label = str(number + 1)
        
        

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)

    @nextcord.ui.button(label='0', style=nextcord.ButtonStyle.gray,emoji="🤷")
    async def count2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        number = int(button.label) if button.label else 0
        
        if number + 1 >= 1:
            button.style = nextcord.ButtonStyle.gray
            button.disabled = False
        button.label = str(number + 1)
        
        

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)

    @nextcord.ui.button(label='0', style=nextcord.ButtonStyle.red,emoji="👎🏼")
    async def count3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        number = int(button.label) if button.label else 0
        
        if number + 1 >= 1:
            button.style = nextcord.ButtonStyle.red
            button.disabled = False
        button.label = str(number + 1)
        
        

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)



    async def interaction_check(self, interaction):
        if interaction.user.id not in self.already_voted:
            self.already_voted.append(interaction.user.id)
            return True

        al_vot = f"Interaction Failed because `It Seems You have already Voted!!`"
        await interaction.response.send_message(al_vot, ephemeral=True)
        return False