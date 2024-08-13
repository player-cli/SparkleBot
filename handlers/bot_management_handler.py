import database
from misc import bot_keyboard

class Admin:

    def __init__(self, bot) -> None:

        self.bot = bot
        self.client_db = database.DataBase("users")
        self.manager_db = database.DataBase("managers")

    def _add_manager(self, message):
        self.bot.send_message(message.chat.id, "Введите cid менеджера которого необходмо добавить")
        self.bot.register_next_step_handler(message, self.__add_manager_next)

    def __add_manager_next(self, message):
        self.manager_db._add(int(message.text), int(message.text))
        self.bot.send_message(message.chat.id, "Менеджер успешно добавлен!", reply_markup = bot_keyboard.admin_keyboard)

    def _remove_manager(self, message):
        self.bot.send_message(message.chat.id, "Введите cid менеджера которого необходмо убрать")
        self.bot.register_next_step_handler(message, self.__remove_manager_next)

    def __remove_manager_next(self, message):
        self.manager_db._remove(message.text)
        self.bot.send_message(message.chat.id, "Менеджер успешно удален!", reply_markup = bot_keyboard.admin_keyboard)
    
    def _stats(self, message):
        self.bot.send_message(message.chat.id, f"Статистика:\nПользователей {len(self.client_db._get_list())}\nМенеджеров {len(self.manager_db._get_list())}", reply_markup = bot_keyboard.admin_keyboard)