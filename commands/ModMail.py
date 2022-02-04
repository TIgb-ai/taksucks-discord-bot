
import nextcord
import asyncio
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions, BadArgument


mails_channel_name = "tak_modmail_logs"

class ModMail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @has_permissions(administrator=True)
    async def setup(self, ctx):
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        channel = nextcord.utils.get(ctx.guild.channels, name=mails_channel_name)
        if channel is None:
            guild = ctx.guild
            overwrites = {
                guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
                guild.me: nextcord.PermissionOverwrite(read_messages=True)
            }

            mod_channel = await guild.create_text_channel(mails_channel_name, overwrites=overwrites)
            embed = nextcord.Embed(
                title='Setup completed',
                description=f"{mod_channel.name} is created.",
                color = nextcord.Color.green(),
            )
        else:
            mod_channel = channel
            embed = nextcord.Embed(
                title='Setup completed',
                description=f"{mod_channel.name} exists",
                color = nextcord.Color.blue(),
            )
        
        await ctx.send(embed=embed)

        overwrites2 = {
            guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
            guild.me: nextcord.PermissionOverwrite(read_messages=True)
        }
        try:
            mod_logs = await guild.create_text_channel("mod-logs", overwrites=overwrites2)
        except:
            print("couldn't create a mod-logs channel, maybe it exists")

    @setup.error
    async def setup_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = nextcord.Embed(
                title='Setup',
                description="You don't have permissions to manage mod mails",
                color = nextcord.Color.red(),
            )
            await ctx.send(embed=embed)
        # else:
        #     embed = nextcord.Embed(
        #         title='Server Only Command',
        #         description="You can't use this command here",
        #         color = nextcord.Color.red(),
        #     )
        #     await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.content.startswith('[]'):
            if isinstance(message.channel, nextcord.channel.DMChannel) and message.author != self.bot.user:
                try:
                    # send to server
                    embed_to = nextcord.Embed(
                        title='Mod Mail Received',
                        description=f"sent by: {message.author} \nmessage: {message.content} \nuser id: {message.author.id}",
                        color = nextcord.Color.blue(),
                    )
                    embed_to.set_footer(text="use reply <id> <message>")
                    mails_channel = self.bot.get_channel(938804736902176818)
                    await mails_channel.send(embed=embed_to)

                    # report result to user
                    embed_reply = nextcord.Embed(
                        title='Mail sent',
                        description=f"Your message has been sent to moderators",
                        color = nextcord.Color.green(),
                    )
                    await message.author.send(embed=embed_reply)
                except:
                    # report result to user
                    embed_reply = nextcord.Embed(
                        title='Sorry 😔',
                        description=f"I couldn't send your message to moderators",
                        color = nextcord.Color.red(),
                    )
                    await message.author.send(embed=embed_reply)

    @commands.command()
    @commands.guild_only()
    @has_permissions(manage_messages=True)
    async def reply(self, ctx, id: int = 0, *, msg: str = "moderator is replying..."):
        await ctx.trigger_typing()
        message = msg
        user = self.bot.get_user(id)
        if user is not None:
            # EMBED report result to user
            embed_reply = nextcord.Embed(
                title='Reply from Moderator',
                # title=f'Replied by {ctx.author.name}',
                description=f"{message}",
                color = nextcord.Color.blue(),
            )
            await user.send(embed=embed_reply)

            # EMBED show results to author
            embed_result= nextcord.Embed(
                title='Message sent succesfully',
                description=f"message sent to {user.name}",
                color = nextcord.Color.green(),
            )
            await ctx.send(embed=embed_result)
        elif user is None:
            # EMBED show results to author
            embed_result = nextcord.Embed(
                title='Failed to send message',
                description=f"can't find user with the id {id}",
                color = nextcord.Color.red(),
            )
            await ctx.send(embed=embed_result)

    @reply.error
    async def reply_error(self, ctx, error):
        if isinstance(error, BadArgument):
            embed = nextcord.Embed(
                title="That's not how you use it",
                description="the correct format is <prefix>reply <id> <message>",
                color = nextcord.Color.red(),
            )
            await ctx.send(embed=embed)
        else:
            embed = nextcord.Embed(
                title='Syntax error',
                description="recheck your command.\nsee help module of the command for details",
                color = nextcord.Color.red(),
            )
            await ctx.send(embed=embed)


def setup(bot): 
    bot.add_cog(ModMail(bot))
    print('Mod Mail Commands Ready!!!')
