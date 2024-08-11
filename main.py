#!/usr/bin/python

#         ██████  ██▓███   ▄▄▄       ██▀███   ██ ▄█▀ ██▓    ▓█████     ▄▄▄▄    ▒█████  ▄▄▄█████▓        #    
#       ▒██    ▒ ▓██░  ██▒▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▓██▒    ▓█   ▀    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒        #
#       ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒██░    ▒███      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░        #
#         ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ ▒██░    ▒▓█  ▄    ▒██░█▀  ▒██   ██░░ ▓██▓ ░         #
#       ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░██████▒░▒████▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░         #
#       ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░ ▒░▓  ░░░ ▒░ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░           #
#       ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░░ ░ ▒  ░ ░ ░  ░   ▒░▒   ░   ░ ▒ ▒░     ░            #
#       ░  ░  ░  ░░         ░   ▒     ░░   ░ ░ ░░ ░   ░ ░      ░       ░    ░ ░ ░ ░ ▒    ░              #
#             ░                 ░  ░   ░     ░  ░       ░  ░   ░  ░    ░          ░ ░                   #
#                                                                           ░                           #

# Import main libs

import os
import telebot
import logging

# Import modules

import database
from misc import bot_says
from misc import bot_keyboard
from handlers import bot_admin_handler
from handlers import bot_client_handler

# Init main vars

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


# Start bot

def main() -> int:
    pass