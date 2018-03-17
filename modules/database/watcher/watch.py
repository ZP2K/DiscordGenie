# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
import re

from discord.ext import commands

from modules.database.tasks.db import set_tasks


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def watch(self, ctx, service="", request=""):
        if ctx.message.channel.id != "424676030389944320":
            await self.client.say("Test")
            return
        if service != "crypto":
            await self.client.say("Invalid service!")
            return
        r = re.search("^(\w+)$", request)
        if not r:
            await self.client.say("Invalid request")
            return
        set_tasks(request)
        await self.client.say("```\nWatch request for Service: {} Request: {} added\n```".format(service, request))


def setup(client):
    client.add_cog(Commands(client))
