from telebot import types

client_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Что вас интересует?", one_time_keyboard=True)
client_keyboard.row(types.KeyboardButton(text='Заказать самостоятельно'))
client_keyboard.row(types.KeyboardButton(text='Заказать через менеджера'))
client_keyboard.row(types.KeyboardButton(text='Химчистка'))
client_keyboard.row(types.KeyboardButton(text='Задать вопрос'))

manager_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
manager_keyboard.row(types.KeyboardButton('Забанить пользователя'))
manager_keyboard.row(types.KeyboardButton('Статистика'))

admin_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
admin_keyboard.row(types.KeyboardButton('Добавить менеджера'))
admin_keyboard.row(types.KeyboardButton('Убрать менеджера'))
admin_keyboard.row(types.KeyboardButton('Статистика'))