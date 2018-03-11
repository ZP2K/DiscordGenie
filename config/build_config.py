# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com

import configparser


def read_api_key():
    config = configparser.ConfigParser()
    config.read('bot.ini')
    return config['discordapi']['token']
