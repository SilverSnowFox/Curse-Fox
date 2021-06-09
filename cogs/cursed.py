import discord
from discord.ext import commands


class Messages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Curse", "curse"])
    async def curse_user(self, ctx, user: discord.Member, arg):

        if ctx.message.guild is None:
            await ctx.send("You can't use this command in DMs!")
            return

        guild_id = ctx.message.guild.id
        user_id = user.id

        from data import SQLUser_cursed
        if SQLUser_cursed.user_is_cursed(guild_id, user_id):
            await ctx.send("This user is already cursed!")
            return

        from data import SQLServer_config
        if not SQLServer_config.can_everyone_curse(guild_id):
            await ctx.send("Only admins can decide your fate.")
            return

        from data import SQLServer_curses
        if not SQLServer_curses.curse_exists(guild_id, arg):
            await ctx.send("Curse doesn't exist!")
            return

        SQLUser_cursed.curse_user(guild_id, user_id, arg)
        await ctx.send(f"{user.mention} has been cursed!")

    @commands.Cog.listener()
    async def on_message(self, message=None):
        # Ignore self command's, DMs and other bots
        if message.guild is None or message.author.bot or message.content.startswith('!!'):
            return

        from data import SQLUser_cursed
        curse = SQLUser_cursed.user_curse(message.guild.id, message.author.id)

        # Checks that user is cursed
        if curse is not None:
            # Get attachments
            attachments = message.attachments

            webhooks = await message.channel.webhooks()
            webhook = discord.utils.get(webhooks, name="Curse Fox")

            # Creates the webhook if not exists
            if webhook is None:
                webhook = await message.channel.create_webhook(name="Curse Fox")

            # In case user only sends an attachment
            if message.content == "":
                for im in attachments:
                    await webhook.send(im.url,
                                       username=message.author.display_name,
                                       avatar_url=message.author.avatar_url)
            else:
                await webhook.send("{} {}".format(message.content, curse[0]),
                                   username=message.author.display_name,
                                   avatar_url=message.author.avatar_url)
                # Attachments if user sent a text
                for im in attachments:
                    await webhook.send(im.url,
                                       username=message.author.display_name,
                                       avatar_url=message.author.avatar_url)

            await message.delete()


def setup(client):
    client.add_cog(Messages(client))
