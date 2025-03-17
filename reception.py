from telebot import types, TeleBot

from button import keyboard, check_btn, social_network
from functions import insert_data, update_applicant, read_applicant, delete_applicant
from keys import TOKEN, admin_id, channel_name

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    send = bot.send_message(msg.from_user.id, "Renessans Ta'lim Universiteti botiga hush kelibsiz!")
    send = bot.send_message(msg.from_user.id, "Iltimos ro'yhatdan o'tish uchun Ism va Familyangizni kiriting!")
    bot.register_next_step_handler(send, name_get)


@bot.message_handler(commands=['getall'])
def get_all_result(msg):
    if msg.from_user.id == admin_id:
        applicants = read_applicant()
        length = len(applicants)
        if length == 0:
            bot.send_message(admin_id, "Ro'yhatdan o'tganlar yo'q!")
        for applicant in applicants:
            bot.send_message(
                admin_id,
                text=f"{applicant[0]} - {applicant[1]} == {applicant[2]}, == {applicant[3]}"
            )


@bot.message_handler(commands=['deleteall'])
def delete_all_result(msg):
    if msg.from_user.id == admin_id:
        delete_applicant()
        bot.send_message(admin_id, "Amringiz bosh ustiga 🙏")


@bot.callback_query_handler(func=lambda x: x)
def query(msg: types.CallbackQuery):
    try:
        if msg.data == "checksub":
            bot.delete_message(msg.message.chat.id, msg.message.id)
            check_user = bot.get_chat_member(channel_name, user_id=msg.from_user.id).status
            if check_user == 'member' or check_user == 'creator' or check_user == 'admin' or check_user == 'administrator':
                send = bot.send_message(msg.from_user.id, "To'liq ism familyangizni yuboring?")
                bot.register_next_step_handler(send, name_get)
            else:
                send = bot.send_message(msg.from_user.id,
                                        "Siz kanalga obuna bo'lmagansiz. Iltimos kanalga obuna bo'ling?",
                                        reply_markup=check_btn)
                bot.register_next_step_handler(send, query)
        else:
            print(msg)
    except Exception as ex:
        pass


def name_get(msg: types.Message):
    user_id = msg.from_user.id
    name = f"{msg.text}"
    insert_data(name=name, user_id=user_id)
    bot.send_message(admin_id, f"{name} user ID: {user_id}")
    send = bot.send_message(msg.from_user.id, "Telefon raqamingizni yuboring 👇", reply_markup=keyboard)
    bot.register_next_step_handler(send, phone_number)


# @bot.callback_query_handler(func=lambda x: x)
def phone_number(msg: types.Message):
    try:
        update_applicant(msg.from_user.id, msg.contact.phone_number)
        bot.send_message(admin_id, f"{msg.from_user.id} - {msg.contact.phone_number}")
        bot.send_message(msg.from_user.id, "Siz ro'yhatdan o'tdingiz")
        bot.send_message(msg.from_user.id,
                         text="Bizni ijtimoiy tarmoqlarda kuzatib boring",
                         reply_markup=social_network)
    except AttributeError:
        send = bot.send_message(msg.from_user.id, "Iltimos ro'yhatdan o'tish uchun Ism va Familyangizni kiriting!")
        bot.register_next_step_handler(send, name_get)
        # send = bot.send_message(
        #     msg.from_user.id,
        #     "Telefon nomeringizni yuboring 👇",
        #     reply_markup=keyboard)
        # bot.send_message(msg.from_user.id, msg.text)
        # bot.register_next_step_handler(send, phone_number)


bot.polling()
