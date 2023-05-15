from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import material_keyboard_inline, size_keyboard, complexity_keyboard, color_keyboard, \
    decoration_keyboard, discount_keyboard, offer_keyboard, final_keyboard
from tgbot.messages.product_messages import messages_from_product
from tgbot.misc.states import WorkState
from tgbot.misc.prices import PRICE_TABLE

product_router = Router()


@product_router.message(CommandStart, StateFilter(None))
async def material_handler(message: Message, state: FSMContext):
    await message.answer(messages_from_product['material'], reply_markup=material_keyboard_inline)
    await state.set_state(WorkState.material)


@product_router.callback_query(StateFilter(WorkState.material))
async def size_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(material=data[1])
    await state.update_data(material_index=int(data[0]))
    await state.set_state(WorkState.size)
    await callback.message.answer(messages_from_product['size'], reply_markup=size_keyboard)


@product_router.callback_query(StateFilter(WorkState.size))
async def complexity_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(size=data[1])
    await state.update_data(size_index=int(data[0]))
    await state.set_state(WorkState.complexity)
    await callback.message.answer(messages_from_product['complexity'], reply_markup=complexity_keyboard)


@product_router.callback_query(StateFilter(WorkState.complexity))
async def color_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(complexity=data[1])
    await state.update_data(complexity_index=int(data[0]))
    await state.set_state(WorkState.color)
    await callback.message.answer(messages_from_product['color'], reply_markup=color_keyboard)


@product_router.callback_query(StateFilter(WorkState.color))
async def decoration_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(color=data[1])
    await state.update_data(color_index=int(data[0]))
    await state.set_state(WorkState.decoration)
    await callback.message.answer(messages_from_product['decoration'], reply_markup=decoration_keyboard)


@product_router.callback_query(StateFilter(WorkState.decoration))
async def discount_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(decoration=data[1])
    await state.update_data(decoration_index=int(data[0]))
    await state.set_state(WorkState.discount)
    await callback.message.answer(messages_from_product['discount'], reply_markup=discount_keyboard)


@product_router.callback_query(StateFilter(WorkState.discount))
async def offer_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(discount=data[1])
    await state.update_data(discount_index=int(data[0]))
    await state.set_state(WorkState.offer)
    await callback.message.answer(messages_from_product['offer'], reply_markup=offer_keyboard)


@product_router.callback_query(StateFilter(WorkState.offer))
async def final_handler(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    price = PRICE_TABLE[int(data['complexity_index'])][int(data['size_index'])]
    print(price)
    if int(data['material_index']) == 2 or int(data['material_index']) == 6:
        price *= 1.3
    else:
        price *= 1.5
    print(price)
    if int(data['color_index']) == 2 or int(data['color_index']) == 3:
        price *= 1.3
    print(price)
    if int(data['decoration_index']) == 0:
        price += 300
    print(price)
    price *= float(data['discount'])
    print(price)
    await callback.message.answer(text="наш вк", reply_markup=final_keyboard)
