import re

from discord.ext import commands

from modules.awslambda import lambda_functions


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def winrate(self, ctx):
        m = re.search('.winrate (\w+)', ctx.message.content)
        position = m.group(1)
        await self.client.say("Fetching winrate for position: {}".format(position))
        lambda_functions.request({"dotabuff": position})
