import datetime

from telebot import types, TeleBot
from telebot.apihelper import send_message

from button import keyboard, check_btn, social_network
from functions import insert_renessans_data, update_renessans_ages, update_renessans_phone, delete_renessans, \
    read_renessans_data, check_user_id
from keys import TOKEN, admin_id, channel_name

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(admin_id, f"{msg.from_user.id} ---{datetime.date.today()} -- {msg.text}")
    if check_user_id(str(msg.from_user.id)):
        check_user = bot.get_chat_member(channel_name, user_id=msg.from_user.id).status
        if check_user == 'member' or check_user == 'creator' or check_user == 'admin' or check_user == 'administrator':
            send = bot.send_message(msg.from_user.id,
                                    "Ism va familyangizni kiriting!")
            bot.register_next_step_handler(send, name_get)
        else:
            bot.send_message(msg.from_user.id,
                             "Telegram kanalga a'zo bo'ling",
                             reply_markup=check_btn)

    else:
        send = bot.send_message(msg.from_user.id, "Siz ro'yhatdan o'tgansiz.")
        bot.register_next_step_handler(send, check_message_user)


@bot.message_handler(commands=['getall'])
def get_all_result(msg):
    if msg.from_user.id == admin_id:
        applicants = read_renessans_data()
        length = len(applicants)
        if length == 0:
            bot.send_message(admin_id, "Ro'yhatdan o'tganlar yo'q!")
        for applicant in applicants:
            bot.send_message(
                admin_id,
                text=f"{applicant[0]} - {applicant[1]} == {applicant[2]}, == {applicant[3]}, == {applicant[4]}, == {applicant[5]}",
            )


@bot.message_handler(commands=['deleteall'])
def delete_all_result(msg):
    if msg.from_user.id == admin_id:
        delete_renessans()
        bot.send_message(admin_id, "Amringiz bosh ustiga 🙏")


@bot.callback_query_handler(func=lambda x: x)
def query(msg: types.CallbackQuery):
    try:
        if msg.data == "checksub":
            bot.delete_message(msg.message.chat.id, msg.message.id)
            check_user = bot.get_chat_member(channel_name, user_id=msg.from_user.id).status
            if check_user == 'member' or check_user == 'creator' or check_user == 'admin' or check_user == 'administrator':
                send = bot.send_message(msg.from_user.id,
                                        "Ism va familyangizni kiriting!")
                bot.register_next_step_handler(send, name_get)
            else:
                send = bot.send_message(msg.from_user.id,
                                        "Siz telegram kanalga a'zo bo'lmagansiz",
                                        reply_markup=check_btn)
                bot.register_next_step_handler(send, query)
        else:
            print(msg)
    except Exception as ex:
        pass


def name_get(msg: types.Message):
    bot.send_message(admin_id, f"{msg.from_user.id} ---{datetime.date.today()} -- {msg.text}")
    user_id = msg.from_user.id
    name = f"{msg.text}"
    insert_renessans_data(
        user_id=user_id,
        name=name,
        ages=" ",
        phone=" ",
        create_at=datetime.date.today())

    send = bot.send_message(msg.from_user.id, "Yoshingizni kiriting!")
    bot.register_next_step_handler(send, user_age)


def user_age(msg: types.Message):
    bot.send_message(admin_id, f"{msg.from_user.id} ---{datetime.date.today()} -- {msg.text}")
    user_id = msg.from_user.id

    ages = f"{msg.text}"
    update_renessans_ages(user_id, ages)
    send = bot.send_message(msg.from_user.id, "Telefon raqamingizni yuboring 👇", reply_markup=keyboard)
    bot.register_next_step_handler(send, phone_number)


# @bot.callback_query_handler(func=lambda x: x)
def phone_number(msg: types.Message):
    try:
        update_renessans_phone(msg.from_user.id, msg.contact.phone_number)
        send = bot.send_message(msg.from_user.id, "Siz ro'yhatdan o'tdingiz. Bizni Ijtimoiy tarmoqlarda kuzatib boring.", reply_markup=social_network)
        bot.register_next_step_handler(send, check_message_user)
    except AttributeError:
        send = bot.send_message(
            msg.from_user.id,
            "Telefon nomeringizni yuboring 👇",
            reply_markup=keyboard)
        bot.register_next_step_handler(send, phone_number)


def check_message_user(msg: types.Message):
    if check_user_id(str(msg.from_user.id)):
        if msg.text == "/deleteall" and msg.from_user.id == admin_id:
            delete_renessans()
            send = bot.send_message(msg.from_user.id, "Amringiz bosh ustiga")
            bot.register_next_step_handler(send, check_message_user)
        elif msg.text == "/getall" and msg.from_user.id == admin_id:
            get_all_result(msg)
            send = bot.send_message(msg.from_user.id, "Barchasi shular :)")
            bot.register_next_step_handler(send, check_message_user)
        elif msg.text == "/start":
            if check_user_id(str(msg.from_user.id)):
                bot.send_message(msg.from_user.id,
                                 "Kanalga obuna bo'ling",
                                 reply_markup=check_btn)
            else:
                send = bot.send_message(msg.from_user.id, "Siz ro'yhatdan o'tgansiz.")
                bot.register_next_step_handler(send, check_message_user)
        else:
            send = bot.send_message(msg.from_user.id, "Siz ro'yhatdan o'tgansiz.")
            bot.register_next_step_handler(send, check_message_user)
    else:
        if msg.text == "/deleteall" and msg.from_user.id == admin_id:
            delete_renessans()
            send = bot.send_message(msg.from_user.id, "Amringiz bosh ustiga")
            bot.register_next_step_handler(send, check_message_user)
        elif msg.text == "/getall" and msg.from_user.id == admin_id:
            get_all_result(msg)
            send = bot.send_message(msg.from_user.id, "Barchasi shular :)")
            bot.register_next_step_handler(send, check_message_user)
        else:
            send = bot.send_message(msg.from_user.id, "Siz ro'yhatdan o'tgansiz.")
            bot.register_next_step_handler(send, check_message_user)


bot.polling()
