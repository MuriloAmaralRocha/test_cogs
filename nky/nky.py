import discord
import re
import snscrape.modules.twitter as sntwitter
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

        wordToSearch = "never kill yourself"
        user = "Showori_"
        query = f'from:{user} "{wordToSearch}"'

        tweet = None
        for t in sntwitter.TwitterSearchScraper(query).get_items():
            tweet = t
            break

        if tweet:
            await message.channel.send(tweet.url)
        else:
            await message.channel.send(
                "https://cdn.discordapp.com/attachments/241369543572848640/1362212240736125050/Never_Kill_yourself.mp4"
            )


def setup(bot):
    bot.add_cog(nky(bot))