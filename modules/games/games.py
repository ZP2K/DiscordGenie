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

    @commands.command(pass_context=True)
    async def roulette(self, ctx):
        r = random.randint(1, 6)
        if r:
            await self.client.say("You were shot. Have fun!")
            txt = ".abuse {} 1".format(ctx.message.author.mention)
            message = await self.client.say(txt)
            self.client.process_commands(message)
        else:
            await self.client.say("You're safe!")


def setup(client):
    client.add_cog(Commands(client))
