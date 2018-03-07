# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.W
import re
import urllib.request

from discord.ext import commands


# place holder, not needed anymore. moved functions to moderation

class Commands:
    def __init__(self, client):
        self.client = client

    # not actually wget
    @commands.command(pass_context=True)
    async def wget(self, ctx):
        if " \"https://raw.githubusercontent.com/complexitydev/" not in ctx.message.content:
            await self.client.say("Invalid")
            return
        if "--code" in ctx.message.content:
            m = re.search('\"(.+?)\"', ctx.message.content)
            request = m.group(1)
            page = str(urllib.request.urlopen(request).read().decode('unicode_escape'))
            text = "```\n" + page + "\n```"
            await self.client.say(text)


def setup(client):
    client.add_cog(Commands(client))
