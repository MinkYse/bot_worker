# -*- coding: utf-8 -*-

from vkbottle.bot import Bot, Message

from environs import Env

env = Env()
env.read_env('.env')

token = env.str("VK_BOT_TOKEN")

client = Bot(token)


@client.on.private_message(text="<msg>")
async def echo_answer(ans: Message, msg):
    await ans.answer(f"Добрый день, благодарим вас за заказ")
    data = list(map(lambda let: let.encode('cp1251').decode('utf8'), ans.ref.split('-')))
    print(data)
    users_info = await client.api.users.get(ans.from_id)
    message = f'У вас новый заказ!!\n\n{users_info[0].first_name} {users_info[0].last_name}\n' + '\n'.join(data)
    await client.api.messages.send(
        peer_id=262672616, message=message, random_id=0
    )

if __name__ == "__main__":
    client.run_forever()