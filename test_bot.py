from discord.ext import commands


def test_api_status():
    client = commands.Bot(command_prefix='.')
    client.run('NDIwMzcyNTU5MzkwMDQ4MjU2.DX-96g.kU-RtfEHRa-Mt8IcxXUifIkGDss')
    assert ("blah" in client.user.name)
