import discord
from discord.ext import commands
import asyncio
import pytz

BotToken = "" #TODO Replace with your bot token
serverID = "" #TODO Replace with your server id
ChanID = "" #TODO Replace with your chan id

#variable
version ="v0.0alpha"
vChannel = "example-bot"

#Create Bot
bot = commands.Bot(command_prefix='!', description='A sample bot')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def info(ctx):
    channel = str(ctx.message.channel.name)
    if channel == vChannel:
        embed = discord.Embed(title="Example Bot", description="A simple Example Bot", color=0xeee657)

        # Personal Info
        embed.add_field(name="Author", value="OakNLeaf")

        # Version Info
        embed.add_field(name="Version", value=version)

        # Version Changes
        embed.add_field(name=version + " changes", value="Initial Alpha Release")

        # Footer
        embed.set_footer(text="Version " + version)

        await ctx.send(embed=embed)
