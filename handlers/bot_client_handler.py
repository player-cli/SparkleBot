import random

from misc import bot_keyboard
from misc import bot_says

class Client:

    def __init__(self, bot,admin: int,  managers: list, last_message_id: int) -> None:
        self.bot = bot
        self.managers = [x[0] for x in managers]
        self.last_message_id = last_message_id
        self.admin = admin

    def _self_order(self, message):
        self.bot.send_message(message.chat.id, bot_says.order, reply_markup = None)
        self.bot.register_next_step_handler(message, self.__forward_to_manager)

    def _manager_order(self, message):
        self.bot.send_message(message.chat.id, bot_says.managerorder, reply_markup = bot_keyboard.startup_bot_keyboard)
        self.bot.send_message(random.choice(self.managers), text = f"Заявка по китаю от @{message.from_user.username}")

    def _shoes_clean(self, message):
        self.bot.send_message(message.chat.id, bot_says.shoesclean, reply_markup = bot_keyboard.startup_bot_keyboard)
        self.bot.send_message(self.managers[0], text = f"Заявка по кроссовкам от @{message.from_user.username}")

    def _qa(self, message):
        self.bot.send_message(message.chat.id, bot_says.help, reply_markup = bot_keyboard.startup_bot_keyboard)

    def __forward_to_manager(self, message):
        self.bot.forward_message(random.choice(self.managers), message.chat.id, message.message_id)
        self.bot.send_message(message.chat.id, "Отправили заявку на покупку, скоро вам напишет менеджер для подтверждения! :3", reply_markup = bot_keyboard.startup_bot_keyboard)

    

    