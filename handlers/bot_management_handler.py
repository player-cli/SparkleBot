from telebot.util import async_list

class Admin:

    def __init__(self, bot) -> None:

        self.bot = bot
user_ids = [123456, 789012, 345678]  # список ID пользователей
message = "Привет, это рассылка!"

async_list(bot.send_message, user_ids, message)

class Manager:

    def __init__(self, bot) -> None:

        self.bot = bot