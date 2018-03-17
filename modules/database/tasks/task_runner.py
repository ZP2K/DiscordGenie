import asyncio

import discord

from .fetch_tasks import get_tasks


async def run_tasks(client):
    await client.wait_until_ready()
    channel = discord.Object(id='422504096990494741')
    while not client.is_closed:
        tasks = get_tasks()
        print(tasks)
        await asyncio.sleep(60)
