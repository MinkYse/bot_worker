from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tgbot.messages.product_messages import size_variants, complexity_variants


def size_choice(call_1, call_2, call_3):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Назад', callback_data=call_1,
                                     disable_notification=True if int(call_1) < 0 else False),
                InlineKeyboardButton(text='Ок', callback_data=f'{call_2}-ok'),
                InlineKeyboardButton(text='Вперёд', callback_data=call_3,
                                     disable_notification=True if int(call_3) > len(
                                         size_variants['messages']) else False)
            ]
        ]
    )
    return keyboard


"""def material_choice(call_1, call_2, call_3):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Назад', callback_data=call_1,
                                     disable_notification=True if int(call_1) < 0 else False),
                InlineKeyboardButton(text='Ок', callback_data=f'{call_2}-ok'),
                InlineKeyboardButton(text='Вперёд', callback_data=call_3,
                                     disable_notification=True if int(call_3) > len(
                                         material_variants['messages']) else False)
            ]
        ]
    )
    return keyboard"""


def complexity_choice(call_1, call_2, call_3):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Назад', callback_data=call_1,
                                     disable_notification=True if int(call_1) < 0 else False),
                InlineKeyboardButton(text='Ок', callback_data=f'{call_2}-ok'),
                InlineKeyboardButton(text='Вперёд', callback_data=call_3,
                                     disable_notification=True if int(call_3) > len(
                                         complexity_variants['messages']) else False)
            ]
        ]
    )
    return keyboard


material_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Хлопок', callback_data="0-хлопок")],
        [InlineKeyboardButton(text='Кожа/Экокожа', callback_data="1-кожа/экокожа")],
        [InlineKeyboardButton(text='Синтетика', callback_data="2-синтетика")],
        [InlineKeyboardButton(text='Вискоза', callback_data="3-вискоза")],
        [InlineKeyboardButton(text='Лён', callback_data="4-лён")],
        [InlineKeyboardButton(text='Деним', callback_data="5-деним")],
        [InlineKeyboardButton(text='Другое', callback_data="6-другое")]
    ],
)

color_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Белое', callback_data="0-белое")],
        [InlineKeyboardButton(text='Скорее светлое', callback_data="1-Скорее светлое")],
        [InlineKeyboardButton(text='Скорее тёмное', callback_data="3-Скорее тёмное")],
        [InlineKeyboardButton(text='Чёрное', callback_data="4-Черное")]
    ]
)

decoration_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да', callback_data="0-с декорациями")],
        [InlineKeyboardButton(text='Нет', callback_data="1-без декораций")]
    ]
)

offer_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Скорее позже', callback_data="0-не сейчас")],
        [InlineKeyboardButton(text='Да!', callback_data="1-сейчас")]
    ]
)

final_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти в вк', url="https://vk.com/tit_com77")
        ]
    ]
)
