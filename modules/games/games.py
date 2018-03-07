# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
import random

from discord.ext import commands


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self):
        r = random.randint(1, 6)
        await self.client.say("You rolled {}!".format(r))


def setup(client):
    client.add_cog(Commands(client))
