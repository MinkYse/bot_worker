from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

material_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Хлопок'),
            KeyboardButton(text='Кожа/Экоожа'),
            KeyboardButton(text='Синтетика')
        ],
        [
            KeyboardButton(text='Вискоза'),
            KeyboardButton(text='Лён'),
            KeyboardButton(text='Что-то')
        ],
        [KeyboardButton(text='Другое')]
    ],
    resize_keyboard=True
)