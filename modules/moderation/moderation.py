# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
import re

from modules.custom_checks.auth import *
from .mod_helpers import *


class Commands:
    def __init__(self, client):
        self.client = client

    @auth_check()
    @commands.command(pass_context=True)
    async def assemble(self, ctx):
        members = await get_favorite_members(ctx)
        if ctx.message.author in members:
            members.remove(ctx.message.author)
        await mention_users(self.client, members)

    @auth_check()
    @commands.command(pass_context=True)
    async def abuse(self, ctx, mention, i=1):
        await abuse_internal(self.client, ctx.message, i)

    @auth_check()
    @commands.command(pass_context=True)
    async def move(self, ctx, group, request):
        request = request.lower()
        members = []
        if group == "x":
            members = await get_favorite_members(ctx)
        else:
            r = re.search("<@(\d+)>", group)
            if not r:
                return
            members.append(ctx.message.server.get_member(r.group(1)))
        channels = self.client.get_all_channels()

        # allow partial matches, not efficient
        for channel in channels:
            if request in channel.name.lower():
                target = channel

        for member in members:
            await self.client.move_member(member, target)

    @auth_check()
    @commands.command(pass_context=True)
    async def kick(self, ctx):
        if not ctx.message.mentions:
            return
        for member in ctx.message.mentions:
            if get_user(member.id) == get_user(ctx.message.author):
                await self.client.say("Only super users can kick other global mods!")
                continue
            await self.client.kick(member)
            await self.client.say("Kicked {}! Request={}".format(member.name, ctx.message.author.name))

    @super_check()
    @commands.command(pass_context=True)
    async def ban(self, ctx):
        for member in ctx.message.mentions:
            await self.client.ban(member)
            await self.client.say("Banned {}! Request={}".format(member.name, ctx.message.author.name))

    @auth_check()
    @commands.command(pass_context=True)
    async def unban(self, ctx):
        for member in ctx.message.mentions:
            await self.client.unban(member)
            await self.client.say("Unbanned {}! Request={}".format(member.name, ctx.message.author.name))

    @super_check()
    @commands.command(pass_context=True)
    async def clear(self, ctx, i=2):
        i = int(i)
        await clear_internal(self.client, ctx.message.channel, i)

    @super_check()
    @commands.command(pass_context=True)
    async def add(self, ctx, mention, rank):
        for member in ctx.message.mentions:
            r = set_user(member.id, rank)
            if not r:
                await self.client.say("Failed to add user!")
                return
            await self.client.say("Added user {}".format(member.name))

    @super_check()
    @commands.command(pass_context=True)
    async def get_users(self, ctx):
        members = get_all_users()
        text = "```\n"
        for name, rank in members:
            member = ctx.message.server.get_member(name)
            text += "{} : {}\n".format(member, rank)
        text += "```\n"
        await self.client.say(text)


def setup(client):
    client.add_cog(Commands(client))