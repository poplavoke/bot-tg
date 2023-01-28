import logging
import config as cf
from aiogram import Bot, Dispatcher, executor, types
ribov_list = [1,2,3,4,5,6,7,8,]
ribov_dict = {"селедка":4, "семга": 56, "Яз": 10}
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
def print_dict (ribov):
    tmp = ""
    for i in ribov:
        tmp += f'{i} : {ribov[i]} \n'
        return tmp

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
    print_dict(ribov_dict)
    args = massege.get_args()
    args = args.split()
    print(ribov_dict[args[0]])
    print(args[1])

    if not args:
        return await tgbot.send_message(massege.chat.id,
                                         f" братан есть сейчас только \n{print_dict(ribov_dict)} рибов"
                                         f"Сколько рибов вы хотите")
    else:
        if args[0] in ribov_dict:
            return await tgbot.send_message(massege.chat.id, f"сорян такой рыбы нет")
        if ribov_dict[args[0]] == 0:
            return await tgbot.send_message(massege.chat.id,
                                            "братан прости риба протухла вся, приходи завтра")
        if args[1].isdigit():
            args[1] = int(args[1])
            if args[1] > ribov_dict[args[0]]:
                return await tgbot.send_message(massege.chat.id,
                                                "слишком много риб хочешь, нет столько")
            else:
                ribov_dict[args[0]] = ribov_dict[args[0]] - args[1]
                return await tgbot.send_message(massege.chat.id, f"смари, есть еще \n{print_dict(ribov_dict)} рибов")
        else:
            return await tgbot.send_message(massege.chat.id,"еще раз скажи сколько рибов")

@dp.message_handler(commands=['add'])
async def send_add_command(massege: types.Message):
 print(massege.chat.id)
 args = massege.get_args()
 if massege.chat.id != 841325577:
     return await tgbot.send_message(massege.chat.id, f"брат ти не продавец")
 if not args:
    return await tgbot.send_message(massege.chat.id, f"сейчас есть {len(ribov_list)} рибов")
 else:
     if args.isdigit():
         args = int(args)
         for i in range(args):
             ribov_list.append(i)
         return await tgbot.send_message(massege.chat.id, f"{len(ribov_list)} рабов имеется.")
     else:
         return await tgbot.send_message(massege.chat.id, "Ой ты ввёл неверное число, сотри и введи нормально!!!")


@dp.message_handler(commands=['print'])
async def send_welcom(massege : types.Message):
    await massege.reply(" _/\ \n"
                        " /||\ \n"
                        "/||||\ \n"
                        "   ||   \n")




if __name__ == '__main__' :
    executor.start_polling(dp, skip_updates = True)