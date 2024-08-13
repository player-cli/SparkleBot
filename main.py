#!/usr/bin/python
# Import main libs

import os # get api token from envirovnment
import telebot # lib for work with telegram api
import logging # logs for telebot

# Import modules

import database # module for work with db
from misc import bot_says # says for bot
from misc import bot_keyboard # inline and reply markup
from handlers import bot_client_handler # handlers for client
from handlers import bot_management_handler # handlers for admins and managers

# Init main vars

bot = telebot.TeleBot(os.getenv("TOKEN")) # init telebot 
logger = telebot.logger # logs for telebot
admin_cid = int(os.getenv("ADMIN_CID")) # get cid of admin

# Init databases

client_db = database.DataBase("users")
banned_db = database.DataBase("banned")
manager_db = database.DataBase("managers")

# Init handler vars

client = bot_client_handler.Client(bot, admin_cid, manager_db._get_list()) # client handlers
admin = bot_management_handler.Admin(bot) # admin handlers
manager = bot_management_handler.Manager(bot) # manager handlers


# Work with telegram api

@bot.message_handler(commands = ['start'])
def bot_start(message):
    clients = client_db._get_list()
    banned = banned_db._get_list()
    managers = manager_db._get_list()
    uid = message.from_user.id
    cid = message.chat.id
    user = [cid, uid]
    if cid != admin_cid:
        if user not in banned:
                if user not in managers:
                    if user in clients:
                        bot.send_message(message.chat.id, text = bot_says.start, reply_markup = bot_keyboard.client_keyboard)
                    else:
                        client_db._add(cid, uid)
                        bot.send_message(message.chat.id, text = bot_says.start, reply_markup = bot_keyboard.client_keyboard)
                else:
                    bot.send_message(message.chat.id, text = f"Добро пожаловать {message.from_user.username}:{message.from_user.id}, вы являетесь менеджером!", reply_markup = bot_keyboard.manager_keyboard)
        else:
            bot.send_message(message.chat.id, text = f"Пользователь {message.from_user.id}, вы не можете пользоваться данным ботом так как вы забанены!")
    else:
        bot.send_message(message.chat.id, text = f"Добро пожаловать {message.from_user.username}:{message.from_user.id}, вы являетесь администратором!", reply_markup = bot_keyboard.admin_keyboard)


@bot.message_handler(commands = ['help'])
def bot_help(message):
    bot.send_message(message.chat.id, text=bot_says.help)

@bot.message_handler(commands = ['devel'])
def bot_devel(message):
    bot.send_message(message.chat.id, text="Бот создал @player_cli")

@bot.message_handler(func=lambda m: True)
def bot_work_handler(message):
    banned = banned_db._get_list()
    managers = manager_db._get_list()
    cid = message.chat.id
    uid = message.from_user.id
    user = [cid, uid]
    if cid != admin_cid and user not in managers and user not in banned:
        match(message.text):
            case 'Заказать самостоятельно':
                client._self_order(message)
            case 'Заказать через менеджера':
                client._manager_order(message)
            case 'Химчистка':
                client._shoes_clean(message)
            case _:
                bot.send_message(cid, "Нет такой команды!")
    if user in managers and user not in banned:
        match(message.text):
            case 'Назад':
                bot.send_message(message.chat.id, text = f"Добро пожаловать {message.from_user.username}:{message.from_user.id}, вы являетесь менеджером!", reply_markup = bot_keyboard.manager_keyboard)
            case _:
                bot.send_message(cid, "Нет такой команды!")
    if cid == admin_cid:
        match(message.text):
            case 'Назад':
                bot.send_message(message.chat.id, text = f"Добро пожаловать {message.from_user.username}:{message.from_user.id}, вы являетесь администратором!", reply_markup = bot_keyboard.admin_keyboard)
            case _:
                bot.send_message(cid, "Нет такой команды!")
    if user in banned:
        bot.send_message(cid, "У вас нет прав пользоваться данным ботом так как вас забанил менеджер/администратор",reply_markup = None)



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
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    bot.polling() # start bot

if __name__ == "__main__": # need
    main()                 # need