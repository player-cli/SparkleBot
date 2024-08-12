from telebot import types

client_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Что вас интересует?", one_time_keyboard=True)
client_keyboard.row(types.KeyboardButton(text='Заказать самостоятельно'))
client_keyboard.row(types.KeyboardButton(text='Заказать через менеджера'))
client_keyboard.row(types.KeyboardButton(text='Химчистка'))

manager_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
manager_keyboard.row(types.KeyboardButton('Забанить пользователя'))
manager_keyboard.row(types.KeyboardButton('Статистика'))

admin_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
admin_keyboard.row(types.KeyboardButton('Добавить менеджера'))
admin_keyboard.row(types.KeyboardButton('Убрать менеджера'))
admin_keyboard.row(types.KeyboardButton('Статистика'))

self_order_inline_keyboard = types.InlineKeyboardMarkup(row_width = 1)
self_order_inline_keyboard.add(types.InlineKeyboardButton("Оставить заявку", callback_data="self_order"))
self_order_inline_keyboard.add(types.InlineKeyboardButton("Назад", callback_data="back"))

manager_order_inline_keyboard = types.InlineKeyboardMarkup(row_width = 1)
manager_order_inline_keyboard.add(types.InlineKeyboardButton("Оставить заявку", callback_data="manager_order"))
manager_order_inline_keyboard.add(types.InlineKeyboardButton("Назад", callback_data="back"))

clean_inline_keyboard = types.InlineKeyboardMarkup(row_width = 1)
clean_inline_keyboard.add(types.InlineKeyboardButton("Оставить заявку на химчистку", callback_data="shoes_clean_order"))
clean_inline_keyboard.add(types.InlineKeyboardButton("Примеры До/После химчистки", callback_data="shoes_clean_examples"))
clean_inline_keyboard.add(types.InlineKeyboardButton("Назад", callback_data="back"))