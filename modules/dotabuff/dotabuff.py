# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com

from discord.ext import commands

from modules.aws_lambda import api


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def winrate(self, ctx, request):
        positions = ["mid", "off", "safe", "jungle", "roaming"]
        if not request or request not in positions:
            usage = "```Usage:\n.dotabuff [mid|off|safe|jungle|roaming]"
            await self.client.say(usage)
        api.process("dotabuff", request)


def setup(client):
    client.add_cog(Commands(client))
