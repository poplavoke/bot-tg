import logging
import config as cf
from aiogram import Bot, Dispatcher, executor, types
ribov_list = [1,2,3,4,5,6,7,8,]
token = cf.token
tgbot = Bot(token)
dp = Dispatcher(tgbot)

help_message = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/bb</b> - <em>прощание</em>
<b>/print</b> - <em>елочка</em>
<b>/buy</b> - <em>покупка рыб</em>
"""
@dp.message_handler(commands =['help'])
async def send_help_command(message: types.Message):
 await tgbot.send_message(message.chat.id, help_message, "HTML")

@dp.message_handler(commands = ['start'])
async def send_welcom_commands(message : types.Message):
   return await tgbot.send_message (message.chat.id,"купи рибу по братски, брат")

@dp.message_handler(commands=['bb'])
async def send_welcom(massege : types.Message):
    await massege.reply("я ухожу, ухожу красиво")

    @dp.message_handler(commands=['buy'])
    async def send_buy_command(massege: types.Message):
        args = massege.get_args()
        if len(ribov_list) == 0:
            return await tgbot.send_massege(massege.chat.id,
                                            "братан прости риба протухла вся, приходи завтра")
        if not args:
            return await tgbot.send_message(massege.chat.id,
                                             f" братан есть сейчас только {len(ribov_list)} рибов"
                                             f"Сколько рибов вы хотите")
        else:
            if args.isdigit():
                args = int(args)
                if args > len(ribov_list):
                    return await tgbot.send_massege(massege.chat.id,
                                                    "слишком много риб хочешь, нет столько")
                else:
                    for i in range(args):
                        ribov_list.pop()
                        return await tgbot.send_massege(massege.chat.id,
                                                        f"смари, есть еще {len(ribov_list)}"
                                                        f"рибов")
                    else:
                        return await tgbot.send_massege(massege.chat.id,"еще раз скажи сколько рибов")






@dp.message_handler(commands=['print'])
async def send_welcom(massege : types.Message):
    await massege.reply(" _/\ \n"
                        " /||\ \n"
                        "/||||\ \n"
                        "   ||   \n")







if __name__ == '__main__' :
    executor.start_polling(dp, skip_updates = True)