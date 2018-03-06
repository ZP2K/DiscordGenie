import re

from discord.ext import commands


class Commands:
    def __init__(self, client):
        self.client = client

    async def mention(self, users):
        to_mention = []
        for member in users:
            to_mention.append(member.mention)
        text = ' '.join(to_mention)
        await self.client.say(text)

    def get_favorite_members(self):
        members = self.client.get_all_members()
        favorites = []
        for member in members:
            # should be stored in config
            if member.name.startswith("Vice") or member.name.startswith("heyo") or member.name.startswith("ben"):
                favorites.append(member)
        return favorites

    @commands.command(pass_context=True)
    async def assemble(self):
        members = self.get_favorite_members()
        await self.mention(members)

    @commands.command(pass_context=True)
    async def move(self, ctx):
        members = self.get_favorite_members()
        channels = self.client.get_all_channels()

        # grab channel name
        m = re.search('.move \"(\w+)\"', ctx.message.content)
        request = m.group(1)
        target = None

        # allow partial matches, not efficient
        for channel in channels:
            if request in channel.name:
                target = channel

        for member in members:
            await self.client.move_member(member, target)


def setup(client):
    client.add_cog(Commands(client))
