# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
from discord.ext import commands


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def watch(self, ctx, service="", request=""):
        if service != "dotabuff" or service != "crypto":
            await self.client.say("Invalid request!")
            return
        await self.client.say("Watch request for {} {} added", service, request)


def setup(client):
    client.add_cog(Commands(client))
