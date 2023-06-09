from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMedia, InputMediaPhoto

from tgbot.keyboards.inline import color_keyboard, decoration_keyboard, offer_keyboard, size_choice, \
    material_keyboard, complexity_choice, final_keyboard_constructor
from tgbot.messages.product_messages import messages_from_product, size_variants, complexity_variants, decoration_photo
from tgbot.misc.prices import PRICE_TABLE
from tgbot.misc.states import WorkState

product_router = Router()


@product_router.message(CommandStart, StateFilter(None))
async def hello_handler(message: Message, state: FSMContext):
    await message.answer('<b>Здравствуйте. Этот бот поможет вам сделать заказ.Хотите ли сделать заказ? </b>',
                         reply_markup=offer_keyboard)


@product_router.callback_query(StateFilter(None), F.data == "1-сейчас")
async def material_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(messages_from_product['material'], reply_markup=material_keyboard)
    await state.set_state(WorkState.material)


@product_router.callback_query(StateFilter(WorkState.material))
async def size_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.set_state(WorkState.size)
    await state.update_data(material=data[1])
    await state.update_data(material_index=int(data[0]))
    file = FSInputFile(fr'tgbot/media/{size_variants["photos"][0]}')
    await callback.message.answer(messages_from_product['size'])
    await callback.message.answer_photo(file, caption=size_variants['messages'][0],
                                        reply_markup=size_choice('-1', '0', '1'),
                                        parse_mode='html')


@product_router.callback_query(StateFilter(WorkState.size), F.data.endswith('ok'))
async def complexity_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.set_state(WorkState.complexity)
    await state.update_data(size=size_variants['messages'][int(data[0])].replace('/', '').replace('<b>', ''))
    await state.update_data(size_index=int(data[0]))
    file = FSInputFile(fr'tgbot/media/{complexity_variants["photos"][0]}')
    await callback.message.answer(messages_from_product['complexity'])
    await callback.message.answer_photo(file, caption=complexity_variants['messages'][0],
                                        reply_markup=complexity_choice('-1', '0', '1'),
                                        parse_mode='html')


@product_router.callback_query(StateFilter(WorkState.size))
async def size_choice_handler(callback: CallbackQuery, state: FSMContext):
    index = int(callback.data)
    if index >= len(size_variants["photos"]):
        index = 0
    elif index < 0:
        index = len(size_variants["photos"]) - 1
    file2 = InputMedia(media=FSInputFile(fr'tgbot/media/{size_variants["photos"][index]}'),
                       caption=size_variants['messages'][index], type='photo')
    await callback.message.edit_media(file2, reply_markup=size_choice(str(index - 1), str(index), str(index + 1)))


@product_router.callback_query(StateFilter(WorkState.complexity), F.data.endswith('ok'))
async def color_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(complexity=complexity_variants['messages'][int(data[0])].replace('/', '').replace('<b>', ''))
    await state.update_data(complexity_index=int(data[0]))
    await state.set_state(WorkState.color)
    await callback.message.answer(messages_from_product['color'], reply_markup=color_keyboard)


@product_router.callback_query(StateFilter(WorkState.complexity))
async def complexity_choice_handler(callback: CallbackQuery, state: FSMContext):
    index = int(callback.data)
    if index >= len(complexity_variants["photos"]):
        index = 0
    elif index < 0:
        index = len(complexity_variants["photos"]) - 1
    file2 = InputMedia(media=FSInputFile(fr'tgbot/media/{complexity_variants["photos"][index]}'),
                       caption=complexity_variants['messages'][index], type='photo')
    await callback.message.edit_media(file2, reply_markup=complexity_choice(str(index - 1), str(index), str(index + 1)))


@product_router.callback_query(StateFilter(WorkState.color))
async def decoration_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(color=data[1])
    await state.update_data(color_index=int(data[0]))
    media = [InputMediaPhoto(types='photo', media=FSInputFile(fr'tgbot/media/{photo}')) for photo in
             decoration_photo]
    await callback.message.answer_media_group(media=media)
    await state.set_state(WorkState.decoration)
    await callback.message.answer(messages_from_product['decoration'], reply_markup=decoration_keyboard)


# todo сделать кнопку, что мы ответили ненадо
@product_router.callback_query(StateFilter(WorkState.decoration))
async def decoration_handler(callback: CallbackQuery, state: FSMContext):
    data = str(callback.data).split('-')
    await state.update_data(decoration=data[1])
    await state.update_data(decoration_index=int(data[0]))
    await state.set_state(WorkState.offer)
    await callback.message.answer(messages_from_product['offer'], reply_markup=offer_keyboard)
    data = str(callback.data).split('-')
    await state.update_data(ansver=data[1])
    # if F.data == "0-не сейчас":
    #     await callback.message.answer()


@product_router.callback_query(StateFilter(WorkState.offer), F.data == "1-сейчас")
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
    await callback.message.answer(text="Итоговая цена заказа: " + str(price))
    print(data)
    await callback.message.answer(text="наш вк", reply_markup=final_keyboard_constructor(
        price,
        data['material'],
        data['size'],
        data['complexity'],
        data['color'],
        data['decoration']
    ))

# todo сделать вывод цены покупателю в сообщении
