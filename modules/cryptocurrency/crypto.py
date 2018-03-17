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
        info = json.loads(aws.process("crypto", request))
        message = '```\n{}:\nUSD: {}\nBTC: {}\n24 Hour Change: {}%\n```'.format(
            info['message'][0]['name'],
            info['message'][0]['price_usd'],
            info['message'][0]['price_btc'],
            info['message'][0]['percent_change_24h'])

        await self.client.say(message)


def setup(client):
    client.add_cog(Commands(client))
