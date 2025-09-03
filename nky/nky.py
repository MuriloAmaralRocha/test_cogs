import discord
import re
from redbot.core import commands

class nky(commands.Cog):
    """Cog that listens for specific words in messages"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """Listens for messages and reacts to certain words"""
        # Don't let the bot respond to its own messages
        if message.author == self.bot.user:
            return
        
        # List of greetings to look for
        words = ["kms", "kill myself", "me matar", "me mata"]
        if not any(re.search(rf'\b{word}\b', message.content.lower()) for word in words):
            return
        
        await message.channel.send(f"https://cdn.discordapp.com/attachments/241369543572848640/1362212240736125050/Never_Kill_yourself.mp4?ex=68019282&is=68004102&hm=85c26be41c922d0364c69b653f67cab2e0d739fc25556c796c156f912f70908d&")
        return

def setup(bot):
    bot.add_cog(nky(bot))