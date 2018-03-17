import asyncio

import discord

from modules.cryptocurrency.crypto import get_info
from modules.moderation.moderation import clear_internal
from .db import get_tasks

messages = {}


async def run_tasks(client):
    await client.wait_until_ready()
    channel = discord.Object(id='422504096990494741')
    clear_internal(client, channel, 10)
    while not client.is_closed:
        tasks = get_tasks()
        for service, request in tasks:
            text = get_info(request)
            if request in messages:
                message = messages[request]
                await client.edit_message(message, text)
                continue
            message = await client.send_message(channel, text)
            messages[request] = message
        await asyncio.sleep(120)
