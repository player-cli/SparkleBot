import time
import random

from misc import bot_keyboard
from misc import bot_says

class Client:

    def __init__(self, bot, admin: int,  managers: list) -> None:
        self.bot = bot
        self.managers = [x[0] for x in managers]
        self.admin = admin
        self.managers.append(self.admin)

    def _self_order(self, message):
        self.bot.send_message(message.chat.id, bot_says.order, reply_markup = bot_keyboard.self_order_keyboard)
        self.bot.register_next_step_handler(message, self.__self_order_choose)

    def _manager_order(self, message):
        self.bot.send_message(message.chat.id, "Вы хотели бы оставить заявку для заказа из Китая с помощью менеджера?", reply_markup = bot_keyboard.self_order_keyboard)
        self.bot.register_next_step_handler(message, self.__manager_order_choose)

    def _shoes_clean(self, message):
        self.bot.send_message(message.chat.id, bot_says.shoesclean, reply_markup = bot_keyboard.startup_bot_keyboard)
        self.bot.register_next_step_handler(message, self.__shoes_clean_choose)

    def __forward_to_manager(self, message):
        self.bot.forward_message(random.choice(self.managers), message.chat.id, message.message_id)
        self.bot.send_message(message.chat.id, "Отправили заявку на покупку, скоро вам напишет менеджер для подтверждения! :3", reply_markup = bot_keyboard.client_keyboard)

    def __self_order_choose(self, message):
        if message.text == 'Заказать самостоятельно':
            self.bot.send_message(message.chat.id, "Пришлите в чат сообщение с ссылк(ой/ами) на товар(ы) или скриншот(ы) (ДЕЛАЙТЕ ЭТО 1 СООБЩЕНИЕМ)", reply_markup = None)
            self.bot.register_next_step_handler(message, self.__forward_to_manager)
        if message.text == 'Назад':
            self.bot.send_message(message.chat.id, text = bot_says.start, reply_markup = bot_keyboard.client_keyboard)

    def __manager_order_choose(self, message):
        if message.text == 'Отправить заявку менеджеру':
            self.bot.send_message(message.chat.id, bot_says.managerorder, reply_markup = bot_keyboard.client_keyboard)
            self.bot.send_message(random.choice(self.managers), text = f"Заявка по китаю от @{message.from_user.username}")
            time.sleep(0.5)
            self.bot.send_message(message.chat.id, text = bot_says.start, reply_markup = bot_keyboard.client_keyboard)
        if message.text == 'Назад':
            self.bot.send_message(message.chat.id, text = bot_says.start, reply_markup = bot_keyboard.client_keyboard)

    def __shoes_clean_choose(self, message):
        if message.text == 'Отправить заявку Никите':
            self.bot.send_message(message.chat.id, "Отправили заявку на химчистку, Никита скоро напишет вам! :3", reply_markup = bot_keyboard.client_keyboard)
            self.bot.send_message(self.admin, text = f"Заявка по кроссовкам от @{message.from_user.username}")
            time.sleep(0.5)
            self.bot.send_message(message.chat.id, text = bot_says.start, reply_markup = bot_keyboard.client_keyboard)
        if message.text == 'Назад':
            self.bot.send_message(message.chat.id, text = bot_says.start, reply_markup = bot_keyboard.client_keyboard)
        


    

    