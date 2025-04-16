import asyncio
import discord

from redbot.core import commands

class nky(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message, ctx):
        if message.guild is None:
            return
        
        if message.content.str.lower() is "kill myself" or message.content.str.lower() is "kms":
            await ctx.send("https://cdn.discordapp.com/attachments/241369543572848640/1362212240736125050/Never_Kill_yourself.mp4?ex=68019282&is=68004102&hm=85c26be41c922d0364c69b653f67cab2e0d739fc25556c796c156f912f70908d&")