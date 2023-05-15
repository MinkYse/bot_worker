from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

material_keyboard_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Хлопок', callback_data="0-хлопок"),
            InlineKeyboardButton(text='Кожа/Экокожа', callback_data="1-кожа/экокожа"),
            InlineKeyboardButton(text='Синтетика', callback_data="2-синтетика")
        ],
        [
            InlineKeyboardButton(text='Вискоза', callback_data="3-вискоза"),
            InlineKeyboardButton(text='Лён', callback_data="4-лён"),
            InlineKeyboardButton(text='Деним', callback_data="5-деним")
        ],
        [InlineKeyboardButton(text='Другое', callback_data="6-другое")]
    ],
)

size_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='5 x 5 См', callback_data="0-5 x 5"),
            InlineKeyboardButton(text='5 x 10 См', callback_data="1-5 x 10"),
            InlineKeyboardButton(text='10 x 10 См', callback_data="2-10 x 10"),
            InlineKeyboardButton(text='10 x 15 См', callback_data="3-10 x 15")
        ],
        [
            InlineKeyboardButton(text='15 x 15 См', callback_data="4-15 x 15"),
            InlineKeyboardButton(text='20 x 15 См', callback_data="5-20 x 15"),
            InlineKeyboardButton(text='20 x 20 См', callback_data="6-20 x 20"),
            InlineKeyboardButton(text='25 x 20 См', callback_data="7-25 x 20")
        ],
        [
            InlineKeyboardButton(text='25 x 25 См', callback_data="8-25 x 25"),
            InlineKeyboardButton(text='30 x 30 См', callback_data="9-30 x 30"),
            InlineKeyboardButton(text='35 x 35 См', callback_data="10-35 x 35"),
        ],
        [InlineKeyboardButton(text='Больше', callback_data="11-больше")]
    ],
)
complexity_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Очень простой', callback_data="0-Очень простой"),
            InlineKeyboardButton(text='Легкий', callback_data="1-Легкий"),
            InlineKeyboardButton(text='Средний', callback_data="2-Средний")

        ],
        [
            InlineKeyboardButton(text='Сложный', callback_data="3-Сложный"),
            InlineKeyboardButton(text='Очень сложный', callback_data="4-Очень сложный"),
            InlineKeyboardButton(text='Надпись', callback_data="5-Надпись")
        ]
    ],
)
color_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Белое', callback_data="0-белое"),
            InlineKeyboardButton(text='Скорее светлое', callback_data="1-Скорее светлое")
        ],
        [
            InlineKeyboardButton(text='Скорее тёмное', callback_data="3-Скорее тёмное"),
            InlineKeyboardButton(text='Чёрное', callback_data="4-Черное")
        ]
    ],
)
discount_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Нет', callback_data="0-без скидки"),
            InlineKeyboardButton(text='5%', callback_data="1-5%"),
            InlineKeyboardButton(text='10%', callback_data="2-10%")
        ],
        [
            InlineKeyboardButton(text='15%', callback_data="3-15%"),
            InlineKeyboardButton(text='20%', callback_data="4-20%"),
            InlineKeyboardButton(text='25%', callback_data="5-25%")
        ]
    ],
)

order_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Скорее позже', callback_data="0-не сейчас")
        ],
        [
            InlineKeyboardButton(text='Да!', callback_data="5-сейчас")
        ]
    ],
)
