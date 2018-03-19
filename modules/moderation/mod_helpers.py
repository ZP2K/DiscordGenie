import asyncio

import discord

from modules.database.tasks.db import set_user


async def mention(bot, users):
    to_mention = []
    for member in users:
        to_mention.append(member.mention)
    text = ' '.join(to_mention)
    await bot.say(text)


def get_favorite_members(bot):
    members = bot.get_all_members()
    favorites = []
    for member in members:
        # should be stored in config
        if member.name.startswith("Vice") \
                or member.name.startswith("heyo") \
                or member.name.startswith("ben") \
                or member.name.startswith("major") \
                or member.name.startswith("Ben"):
            favorites.append(member)
    return favorites


async def abuse_internal(bot, message, i: int = 1):
    members = get_favorite_members(bot)
    if message.author not in members:
        return

    if len(message.mentions) < 1:
        await bot.say("```\n"
                      "You didn't mention anyone.\nUsage:"
                      "\n.[c] [mentioned user] [number of iterations optional]\n```")
        return

    if i > 3:
        i = 3

    for member in message.mentions:
        prev_channel = member.voice.voice_channel
        for x in range(0, i):
            for channel in bot.get_all_channels():
                if channel.type == discord.ChannelType.voice:
                    await bot.move_member(member, channel)
                    await asyncio.sleep(.2)
            await asyncio.sleep(.2)
    # move the user back to the original channel
    await bot.move_member(member, prev_channel)


async def clear_internal(bot, channel, count):
    messages = []
    async for x in bot.logs_from(channel, limit=count):
        messages.append(x)
    await bot.delete_messages(messages)


async def get_user_pos(user):
    return get_user_pos(user)


async def set_user_pos(user, role):
    set_user(user, role)
