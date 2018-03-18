# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com

import json
import time

from discord.ext import commands

from modules.aws_lambda import aws


def get_message(info):
    message = '```{}\n{}:\nUSD: {}\nBTC: {}\n1 Hour Change: {}%\n24 Hour Change: {}%\n7 Day Change: {}%\n```'.format(
        time.ctime(),
        info['message'][0]['name'],
        info['message'][0]['price_usd'],
        info['message'][0]['price_btc'],
        info['message'][0]['percent_change_1h'],
        info['message'][0]['percent_change_24h'],
        info['message'][0]['percent_change_7d'])
    return message


def get_info(request):
    info = json.loads(aws.process("crypto", request))
    if 'error' in info['message']:
        return "error"
    return info


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def check(self, ctx, request):
        if ctx.message.channel.id != "424676030389944320":
            return
        info = get_info(request)
        if info == "error":
            await self.client.say("Error processing. Don't use the symbol name!")
        message = get_message(info)
        await self.client.say(message)

    @commands.command(pass_context=True)
    async def convert(self, ctx, request, amount):
        info = get_info(request)
        if info == "error":
            await self.client.say("Error processing. Don't use the symbol name!")
        total = info['message'][0]['price_usd'] * amount
        message = "```\n{}{} : ${}\n```".format(amount, request, total)
        await self.client.say(message)


def setup(client):
    client.add_cog(Commands(client))
