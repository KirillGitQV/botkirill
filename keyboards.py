from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура с отправкой местоположения (Запрашивает местоположение пользователя)
my_geo_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Моё местоположение 🌍', request_location=True))

# Клавиатура с двумя кнопками
button_Nikolai = KeyboardButton('Ленин')
button_Stalin = KeyboardButton('Сталин')
Lenin_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_Stalin).add(button_Nikolai)

button_Putin = KeyboardButton('Путин')
button_Lenin = KeyboardButton('Ленин')
stalin_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_Lenin).add(button_Putin)


# Клавиатура кнопка назад
button_back = KeyboardButton('⬅ Назад')
back_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)