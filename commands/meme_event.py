import asyncio
from os import remove
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from nextcord.ext.commands.cooldowns import BucketType
import nextcord
from requests import delete
import asyncio




meme_terms = "**You can post your memes below:**\n\n> - No Religious or racism memes. Nudity content is strictly prohibited\n> - No useless shit posting including your opinions, random screenshots, flooding replies etc.\n> Contact Mods in <#906485879999193088> if you wanna get some help, No such chaos here\n> No links allowed..."






class meme_event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.Cog.listener()
    async def on_message(self, message):
        meme_event = self.bot.get_channel(977769687750426644)
        upvote = self.bot.get_emoji(977778895090753577)
        downvote = self.bot.get_emoji(977778895497617478)
        if message.channel is meme_event:
            if message.attachments:
                    await message.add_reaction(upvote)
                    await message.add_reaction(downvote)
                    await asyncio.sleep(1)
                    sigma = await message.channel.send(meme_terms)
                    await sigma.pin()
                    
                    return
            else:
                if message.author is self.bot.user:
                    return
                else:
                    await asyncio.sleep(30)
                    print("Deleted Message :")
                    print(f"{message.author} -  {message.content}")
                    await message.delete()
                
                
        
        else:
            pass
        
        
        
def setup(bot):
    bot.add_cog(meme_event(bot))
    print("EVENt Commands Ready")