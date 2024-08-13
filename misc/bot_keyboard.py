from telebot import types

client_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Что вас интересует?", one_time_keyboard=True)
client_keyboard.row(types.KeyboardButton(text='Заказать самостоятельно'))
client_keyboard.row(types.KeyboardButton(text='Заказать через менеджера'))
client_keyboard.row(types.KeyboardButton(text='Химчистка'))

admin_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
admin_keyboard.row(types.KeyboardButton('Добавить менеджера'))
admin_keyboard.row(types.KeyboardButton('Убрать менеджера'))
admin_keyboard.row(types.KeyboardButton('Статистика'))

self_order_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
self_order_keyboard.row(types.KeyboardButton('Заказать самостоятельно'))
self_order_keyboard.row(types.KeyboardButton('Назад'))

manager_order_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
manager_order_keyboard.row(types.KeyboardButton('Отправить заявку менеджеру'))
manager_order_keyboard.row(types.KeyboardButton('Назад'))

clean_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
clean_keyboard.row(types.KeyboardButton('Отправить заявку Никите'))
clean_keyboard.row(types.KeyboardButton('Примеры чистки'))
clean_keyboard.row(types.KeyboardButton('Назад'))