# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com

import json

from discord.ext import commands

from modules.aws_lambda import aws


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def check(self, ctx, request):
        price = aws.process("crypto", request)
        d = json.loads(price)
        print(d)
        # await self.client.say("Price for {} is {}".format(request, price))


def setup(client):
    client.add_cog(Commands(client))
