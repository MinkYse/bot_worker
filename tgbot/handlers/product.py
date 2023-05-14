from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.misc.states import WorkState
from tgbot.keyboards.reply import material_keyboard
from tgbot.keyboards.inline import material_keyboard_inline, size_keyboard
from tgbot.messages.product_messages import messages_from_product

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
async def size_handler(callback: CallbackQuery, state: FSMContext):
    print(22)