# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
from discord.ext import commands

from .mod_helpers import *


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def assemble(self, ctx):
        members = get_favorite_members(self.client)
        if ctx.message.author not in members:
            return
        await self.mention(members)

    @commands.command(pass_context=True)
    async def abuse(self, ctx, mention="", i=0):
        await abuse_internal(self.client, ctx.message, i)

    @commands.command(pass_context=True)
    async def move(self, ctx, request):
        request = request.lower()
        members = get_favorite_members(self.client)
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
            await self.client.say("Request failed! Minimum two messages to delete")
            return
        i = int(i)
        await clear_internal(self.client, ctx.message.channel, i)

    @commands.command(pass_context=True)
    async def add(self, ctx, rank):
        await self.client.say("{}".format(ctx.message.author.id))
        req = await get_user_pos(ctx.message.author.id)
        if req != 4:
            await self.client.say("You are not authorized!")
            return
        for member in ctx.message.mentions:
            await set_user_pos(member.id, rank)
            await self.client.say("Added user {}".format(member.name))


def setup(client):
    client.add_cog(Commands(client))
