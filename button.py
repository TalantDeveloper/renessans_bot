from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from keys import channel_url, get_number, instagram_url

check_btn = types.InlineKeyboardMarkup(row_width=1)

check_btn.add(
    types.InlineKeyboardButton(text="A'zo bo'lish", url=channel_url),
    types.InlineKeyboardButton(text="✅ Ro'yhatdan o'tish", callback_data="checksub"),
)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.add(KeyboardButton(get_number, request_contact=True))

social_network = types.InlineKeyboardMarkup(row_width=1)

social_network.add(
    types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/renessans.edu.uz/"),
    types.InlineKeyboardButton(text="Facebook",
                               url="https://www.facebook.com/people/Renessans-University/61557702814655/"),
    types.InlineKeyboardButton(text="Web sayt", url="https://renessans-edu.uz/"),
)

phone_number = types.InlineKeyboardMarkup(row_width=1)

phone_number.add(
    types.InlineKeyboardButton("Telefon raqamingizni kiriting", )
)
