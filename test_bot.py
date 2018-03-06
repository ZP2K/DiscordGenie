from discord.ext import commands

client = commands.Bot(command_prefix='.')
extensions = ["commands"]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('-------------')


@client.command()
async def load(extension_name: str):
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await client.say("{} loaded.".format(extension_name))


def test_api_status():
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.run('NDIwMzcyNTU5MzkwMDQ4MjU2.DX-96g.kU-RtfEHRa-Mt8IcxXUifIkGDss')
