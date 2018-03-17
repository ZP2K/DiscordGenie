# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
import discord
from discord.ext import commands

from config.build_config import read_api_key

client = commands.Bot(command_prefix='.')
extensions = ["modules.moderation.moderation",
              "modules.games.games",
              "modules.dotabuff.dotabuff",
              "modules.cryptocurrency.crypto",
              "modules.database"]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('-------------')
    await client.change_presence(game=discord.Game(name="Ready for commands!"), afk=False)
    print('Ready for commands')

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
            print('Loaded extension {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.run(read_api_key())
