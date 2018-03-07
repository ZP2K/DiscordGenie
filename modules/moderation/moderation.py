# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
import asyncio
import re

import discord
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
            if member.name.startswith("Vice") \
                    or member.name.startswith("heyo") \
                    or member.name.startswith("ben") \
                    or member.name.startswith("major"):
                favorites.append(member)
        return favorites

    @commands.command(pass_context=True)
    async def assemble(self, ctx):
        members = self.get_favorite_members()
        if ctx.message.author not in members:
            return
        await self.mention(members)

    @commands.command(pass_context=True)
    async def abuse(self, ctx):
        members = self.get_favorite_members()
        if ctx.message.author not in members:
            return

        if not ctx.message.mentions:
            return

        for member in ctx.message.mentions:
            prev_channel = member.voice.voice_channel
            for channel in self.client.get_all_channels():
                if channel.type == discord.ChannelType.voice:
                    await self.client.move_member(member, channel)
                    await self.client.send_message(member, 'Get fucked')
                    await asyncio.sleep(.5)
        # move the user back to the original channel
        await self.client.move_member(member, prev_channel)

    @commands.command(pass_context=True)
    async def move(self, ctx):
        members = self.get_favorite_members()
        channels = self.client.get_all_channels()

        if ctx.message.author not in members:
            return

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

    @commands.command(pass_context=True)
    async def kick(self, ctx):
        global_mods = ["95321801344679936", "95582503061954560", "177934831416639488"]
        protected = ["95321801344679936", "95582503061954560"]
        if ctx.message.author.id not in global_mods:
            await self.client.say("You are not permitted!")
            return
        if not ctx.message.mentions:
            return
        for member in ctx.message.mentions:
            if member.id in protected and ctx.message.author.id != "95321801344679936":
                await self.client.say("Only protected users can kick other global mods!")
                continue
            await self.client.kick(member)


def setup(client):
    client.add_cog(Commands(client))
