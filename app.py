'''
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot
'''

from discord import Intents
from discord.ext import commands

from src.utils import utils

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   case_insensitive=True)

cog_dict = {
    'Auto Commands': 'src.cogs.autoCommands',
    'Admin Commands': 'src.cogs.adminCommands',
    'API Based Commands': 'src.cogs.apiBasedCommands',
    'Other Commands': 'src.cogs.otherCommands'
}

def load_cogs(cog_dict: dict):
    """ Function for loading cogs """
    try:
        for key, value in cog_dict.items():
            print(f'[INFO]: Loading... {key}')
            bot.load_extension(value)
    except Exception as e:
        print(f'\n[INFO]: {type(e).__name__} - {e}')


if __name__ == '__main__':
    load_cogs(cog_dict)
    bot.run(utils.DISCORD_TOKEN)
