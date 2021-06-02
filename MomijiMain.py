import discord
import asyncio
import CurseMomiji as MFn
import json_update
import json_update as ju

from discord import utils
from discord.ext import commands
from discord.ext.commands import has_permissions

command_prefix = ["m!"]
client = commands.Bot(command_prefix)
client.remove_command('help')
main_path = "MomijiCurse.json"

Universe = MFn.load_json(main_path)


@client.event
async def on_ready():  # shell responds when ready
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("with some spells."))
    print("Heyo")


@client.event
async def on_guild_join(guild):
    global Universe
    Universe = MFn.new_section(Universe, guild.id)
    ju.jupdate(Universe, main_path)
    print("New guild added")


@client.event
async def on_guild_leave(guild):
    global Universe
    Universe = Universe.pop(str(guild.id))
    ju.jupdate(Universe, main_path)
    print("Guild removed")


@client.command()
async def say(ctx, channel_id, *, msg):
    if isinstance(ctx.channel, discord.channel.DMChannel) and ctx.author.id == 231580977405624320:
        channel = client.get_channel(int(channel_id))
        await channel.send(msg)


@client.command(pass_context=True, aliases=["Help"])
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name='Here are my commands!')

    all_curses = command_prefix[0] + "curses [user] [curse]\n\nCurses someone with one of the following:"
    all_curses.join(MFn.get_curses(Universe[str(ctx.guild.id)]))

    embed.add_field(name='Curse',
                    value=all_curses,
                    inline=False)
    embed.add_field(name="Cure",
                    value=command_prefix[0]+"cure [user]\n\nAdmin only command that cures the user",
                    inline=False)
    embed.add_field(name="Heal",
                    value=command_prefix[0]+"heal [user]\n\nCures any user except yourself!",
                    inline=False)
    embed.add_field(name="CreateCurse",
                    value=command_prefix[0]+"CreateCurse [curse]\n\nAdministrator only command that creates a curse",
                    inline=False)
    embed.add_field(name="DeleteCurse",
                    value=command_prefix[0]+"DeleteCurse [curse]\n\nAdministrator only command that deletes a curse",
                    inline=False)

    channel = await author.create_dm()
    await channel.send(embed=embed)
    await ctx.send("Sent you a DM!")


@client.command(pass_context=True, aliases=["Cure"])
@has_permissions(administrator=True)
async def cure(ctx, member: discord.Member = None):

    if member is None:
        await ctx.send("Invalid argument Please tag a user!\n\n `k!cure [user]`")
    elif member.bot:
        await ctx.send("You can't curse a bot!")
    else:
        if MFn.is_cursed(Universe[str(ctx.guild.id)]["users"], member.id):
            MFn.clear_curse(Universe[str(ctx.guild.id)], member.id)
            await ctx.send('{} is cured with with the power of magic!'.format(member.mention))
        else:
            await ctx.send("Not even magic can help if they aren't cursed")
    ju.jupdate(Universe, main_path)


@cure.error
async def cure_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing permissions")


@client.command(aliases=["Heal"])
async def heal(ctx, member: discord.Member = None):
    guild_id = ctx.guild.id
    if member is None:
        await ctx.send("Please select a member to heal!\n `k!heal [user]`")
    else:
        if not MFn.is_cursed(Universe[str(ctx.guild.id)]["users"], ctx.author.id):
            if MFn.is_cursed(Universe[str(ctx.guild.id)]["users"], member.id):
                MFn.clear_curse(Universe[str(ctx.guild.id)], member.id)
                await ctx.send('{} is cured!'.format(member.mention))
            else:
                await ctx.send("{} wasn't cursed!".format(member.mention))
        else:
            await ctx.send("You are cursed! Only others can help you.")
    ju.jupdate(Universe, main_path)


@client.command(aliases=["Curse"])
async def curse(ctx, member: discord.Member = None, *, arg=None):
    guild_id = ctx.guild.id
    # Checks if user was mentioned
    if member is None:
        await ctx.send("Invalid argument Please tag a user!\n\n `k!curse [user] [curse]`")
    # Checks if cursed was selected
    elif arg is None:
        await ctx.send("Invalid argument! Please select a curse!\n\n `k!curse [user] [curse]`\n")
    # Checks that mentioned isn't already Cursed.
    elif not MFn.is_cursed(Universe[str(ctx.guild.id)]["users"], member.id):
        if MFn.curse_exists(arg, Universe[str(ctx.guild.id)]):
            text = MFn.curse_user(arg, Universe[str(ctx.guild.id)], member.id)
            await ctx.send(text.format(member.mention))
        else:
            await ctx.send("Please select an existing curse!\n")
    else:
        await ctx.send("Already cursed!")
    ju.jupdate(Universe, main_path)


@curse.error
async def curse_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("User does not exist or was not selected")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please try again")


@client.command(pass_context=True, aliases=["CreateCurse", "createcurse"])
@has_permissions(administrator=True)
async def create_curse(ctx, *, new_curse):
    global Universe
    await ctx.send("Welcome to curse creator! Please enter the curse description:\n"
                   "¬ Writing {} will ping the user\n\n"
                   "Example:\n> {} was cursed\nWill result in\n> [cursed user] was cursed")

    def check(msg):
        return ctx.author == msg.author

    try:
        msg = await client.wait_for("message", check=check, timeout=30)
        Universe[str(ctx.guild.id)]["curses"][new_curse] = msg.content
        json_update.jupdate(Universe, main_path)
        await ctx.send("Curse added")
    except asyncio.TimeoutError:
        await ctx.send("Sorry, {} didn't reply in time!" .format(ctx.author.mention))


@client.command(pass_context=True, aliases=["DeleteCurse", "deletecurse"])
@has_permissions(administrator=True)
async def delete_curse(ctx, *, message):
    if MFn.curse_exists(message, Universe[str(ctx.guild.id)]):
        Universe[str(ctx.guild.id)]["curses"].pop(message)
        ju.jupdate(Universe, main_path)
        await ctx.send("Curse has been erased!")
    else:
        await ctx.send("I cannot erase that which does not exist")


@client.listen('on_message')
async def on_message(message):

    allow = True

    # Check if user not a bot
    if message.author.bot:
        return
    # Ignores if message is a command
    for prefix in command_prefix:
        if prefix in message.content:
            allow = False
    # Checks that user is Cursed
    if isinstance(message.channel, discord.channel.DMChannel):
        return

    attach = message.attachments
    guild_id = message.guild.id

    if MFn.is_cursed(Universe[str(guild_id)]["users"], message.author.id) and allow:

        curse_x = Universe[str(guild_id)]["users"][str(message.author.id)]
        webhooks = await message.channel.webhooks()
        webhook = utils.get(webhooks, name="Curse Fox")

        if webhook is None:
            webhook = await message.channel.create_webhook(name="Curse Fox")
        if message.content == "":
            for im in attach:
                await webhook.send(im.url, username=message.author.display_name, avatar_url=message.author.avatar_url)
        else:
            await webhook.send(MFn.cursed_message(message.content, curse_x),
                               username=message.author.display_name,
                               avatar_url=message.author.avatar_url)
            # Attachments
            for im in attach:
                await webhook.send(im.url, username=message.author.display_name, avatar_url=message.author.avatar_url)

        await message.delete()


client.run('ODM0MTQxNTcwNjA0MzM1MTA0.YH8k4A.LEyGU3DB8q83wG3-tFaNMcuBrNw')
