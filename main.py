#!/usr/bin/python
# Import main libs

import os # get api token from envirovnment
import time # need
import telebot # lib for work with telegram api
import logging # logs for telebot

# Import modules

import database # module for work with db
from misc import bot_says # says for bot
from misc import bot_keyboard # inline and reply markup
from handlers import bot_client_handler # handlers for client
from handlers import bot_management_handler # handlers for admins and managers

# Init main vars

bot = telebot.TeleBot(os.getenv("BOT_TOKEN")) # init telebot 
logger = telebot.logger # logs for telebot
admin_cid = os.getenv("ADMIN_CID") # get cid of admin

# Init handler vars

client = bot_client_handler.Client(bot) # client handlers
admin = bot_management_handler.Admin(bot) # admin handlers
manager = bot_management_handler.Manager(bot) # manager handlers

# Init databases

client_db = database.DataBase("users")
manager_db = database.DataBase("managers")

# Start bot

def main() -> int: # press "F" C++
    print("""
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
    """) # da.
    telebot.logger.basicConfig(filename=f'./logs/{time.strptime}.log', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
    bot.polling() # start bot

if __name__ == "__main__": # need
    main()                 # need