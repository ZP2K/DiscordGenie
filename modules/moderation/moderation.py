# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
import asyncio

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
    async def abuse(self, ctx, mention="", i=0):
        if not isinstance(i, int) or i == 0:
            i = 1

        members = self.get_favorite_members()

        if ctx.message.author not in members:
            return

        if len(ctx.message.mentions) < 1:
            await self.client.say("```\n"
                                  "You didn't mention anyone.\nUsage:"
                                  "\n.[c] [mentioned user] [number of iterations optional]\n```")
            return

        i = int(i)
        for member in ctx.message.mentions:
            prev_channel = member.voice.voice_channel
            for x in range(0, i):
                for channel in self.client.get_all_channels():
                    if channel.type == discord.ChannelType.voice:
                        await self.client.move_member(member, channel)
                        await asyncio.sleep(.2)

        # move the user back to the original channel
        await self.client.move_member(member, prev_channel)

    @commands.command(pass_context=True)
    async def move(self, ctx, request):
        request = request.lower()
        members = self.get_favorite_members()
        channels = self.client.get_all_channels()

        if ctx.message.author not in members:
            return

        target = None
        # allow partial matches, not efficient
        for channel in channels:
            if request in channel.name.lower():
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
            await self.client.say("Kicked {}! Request={}".format(member.name, ctx.message.author.name))

    @commands.command(pass_context=True)
    async def ban(self, ctx):
        if ctx.message.author.id != "95321801344679936":
            return

        for member in ctx.message.mentions:
            await self.client.ban(member)
            await self.client.say("Banned {}! Request={}".format(member.name, ctx.message.author.name))

    @commands.command(pass_context=True)
    async def unban(self, ctx):
        if ctx.message.author.id != "95321801344679936":
            return

        for member in ctx.message.mentions:
            await self.client.unban(member)
            await self.client.say("Unbanned {}! Request={}".format(member.name, ctx.message.author.name))
    
    @commands.command(pass_context=True)
    async def clear(self, ctx, i):
        if ctx.message.author.id != "95321801344679936":
            return
        if not i or int(i) <= 1:
            await self.client.say("Request failed! Minimum two messages to delete, or you do not meet the permissions")
            return
        i = int(i)

        messages = []
        async for x in self.client.logs_from(ctx.message.channel, limit=i):
            messages.append(x)
        await self.client.delete_messages(messages)
        await self.client.say("Cleared {} messages! Request={}".format(i, ctx.message.author.name))


def setup(client):
    client.add_cog(Commands(client))
