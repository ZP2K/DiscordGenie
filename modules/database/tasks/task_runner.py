import asyncio

import discord

from modules.cryptocurrency.crypto import get_info
from .db import get_tasks


async def run_tasks(client):
    await client.wait_until_ready()
    channel = discord.Object(id='422504096990494741')
    while not client.is_closed:
        tasks = get_tasks()
        for service, request in tasks:
            message = get_info(request)
            await client.send_message(channel, message)
        await asyncio.sleep(65)
