from discord.ext import commands


# tests whether or not this bot can reach the discord end with a test key


def test_api_status():
    client = commands.Bot(command_prefix='.')
    client.run('NDIwMzcyNTU5MzkwMDQ4MjU2.DX-96g.kU-RtfEHRa-Mt8IcxXUifIkGDss')
    assert ("Blah" in client.user.name)
