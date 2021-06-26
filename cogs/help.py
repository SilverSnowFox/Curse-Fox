import discord
from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Help"])
    async def help(self, ctx):
        user_name = ctx.message.author.name
        guild = ctx.message.guild
        embed = discord.Embed(title=f"Hey {user_name}! Here are my commands and some information!",
                              colour=discord.Colour.dark_purple())
        embed.add_field(name="Cursing Users",
                        value="You can curse someone using !!Curse <user> with an existing curse in the server. " +
                              f"Ex: !!Curse {user_name} nya\n\n",
                        inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="Curing Users",
                        value="`!!Cure <user>` cures the mentioned user from the curse. This command is enabled for " +
                              "everyone by default to all users. It can be changed to only administrators only. " +
                              f"Ex: !!Cure {user_name}\n\n" +
                              "Administrators can also use !!MassCure to cure everyone in the server.",
                        inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="Creating and Deleting Curses",
                        value="You can create a curse by using `!!Create <curse>` with at most 20 characters, and " +
                              "delete one with `!!Delete <curse>`\n" +
                              "Ex: `!!Create nya` and `!!Delete nya`\n\nPlease be aware that these are administrator" +
                              " only commands.",
                        inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="Information",
                        value="You can use `!!Curses` to display all of the guild's curses.",
                        inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="Permissions",
                        value="`!!EveryoneCure <true/false>` toggles everyone's permission to cure others. If set " +
                              "to false, only people without curse and administrators can cure others.\n\nToggles " +
                              "everyone's permission to curse others. If set to false, only administrators can " +
                              "curse others.",
                        inline=False)

        from data import SQLServer_config
        cure = SQLServer_config.can_everyone_cure(guild.id)
        curse = SQLServer_config.can_everyone_curse(guild.id)

        embed.add_field(name=f"Current settings for {guild.name}",
                        value="Everyone can cure is set to {}\nEveryone can curse is set to {}".format(cure, curse),
                        inline=False)

        await ctx.message.author.send(embed=embed)
        await ctx.send("Sent you a DM!")


def setup(client):
    client.add_cog(Guilds(client))
