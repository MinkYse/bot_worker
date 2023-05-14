from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


material_keyboard_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Хлопок', callback_data="0-хлопок"),
            InlineKeyboardButton(text='Кожа/Экоожа', callback_data="1"),
            InlineKeyboardButton(text='Синтетика', callback_data="2")
        ],
        [
            InlineKeyboardButton(text='Вискоза', callback_data="3"),
            InlineKeyboardButton(text='Лён', callback_data="4"),
            InlineKeyboardButton(text='Деним', callback_data="5")
        ],
        [InlineKeyboardButton(text='Другое', callback_data="6")]
    ],
)

size_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='5 x 5 См', callback_data="0-5 x 5"),
            InlineKeyboardButton(text='5 x 10 См', callback_data="1"),
            InlineKeyboardButton(text='10 x 10 См', callback_data="2"),
            InlineKeyboardButton(text='10 x 15 См', callback_data="2")
        ],
        [
            InlineKeyboardButton(text='15 x 15 См', callback_data="0-хлопок"),
            InlineKeyboardButton(text='20 x 15 См', callback_data="1"),
            InlineKeyboardButton(text='20 x 20 См', callback_data="2"),
            InlineKeyboardButton(text='25 x 20 См', callback_data="2")
        ],
        [
            InlineKeyboardButton(text='25 x 25 См', callback_data="0-хлопок"),
            InlineKeyboardButton(text='30 x 30 См', callback_data="1"),
            InlineKeyboardButton(text='35 x 35 См', callback_data="2"),
        ],
        [InlineKeyboardButton(text='Больше', callback_data="2")]
    ],
)