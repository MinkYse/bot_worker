from vkbottle.bot import Bot, Message


api = 'd60bce7c3b428907f3ed0c4ca57eb84c013d90fdb1f61d60d8dbdfbef1c2041ce6978a3cfc266aca1d67f'

bot = Bot(token=api)


@bot.on.message()
async def hi_handler(message: Message):
    print(message.ref)
    users_info = await bot.api.users.get(message.from_id)
    text = str(message.ref).split('|')
    for t in text:
        await message.answer(t.encode().decode('utf-8'))

bot.run_forever()
