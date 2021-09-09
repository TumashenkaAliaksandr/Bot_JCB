import re
import telebot
import book
from string import Template
from telebot import types
import config

# РУССКОЕ МЕНЮ
rMenu = book.russian_menu
# АНГЛИЙСКОЕ МЕНЮ
eMenu = book.english_menu

bot = telebot.TeleBot(config.TOKEN1)

# регистрация пользователя
user_dict = {}


class User:
    def __init__(self, nickname, photo, document):
        self.nickname = nickname
        self.photo = photo
        self.document = document

        keys = book.keyReg

        for key in keys:
            self.key = None


@bot.message_handler(commands=["reg"])
def user_reg(message):
    chat_id = message.chat.id

    if message.text == '/reg':
        bot.send_message(chat_id, 'Напишите свой ник нейм: ')
        bot.register_next_step_handler(message, user_reg)
        return

    user_dict[chat_id] = User(message.text, message.photo, message.document)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Минск')
    btn2 = types.KeyboardButton('Витебск')
    btn3 = types.KeyboardButton('Гомель')
    btn4 = types.KeyboardButton('Гродно')
    btn5 = types.KeyboardButton('Могилев')
    btn6 = types.KeyboardButton('Брест')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    msg = bot.send_message(message.chat.id, book.regCity, reply_markup=markup)
    bot.send_sticker(message.chat.id, book.sticker5)
    bot.send_message(message.chat.id, book.regCity1)
    bot.register_next_step_handler(msg, process_city_step)


def process_city_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.city = message.text

    # удалить старую клавиатуру
    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(chat_id, 'Пришлите фото авто:', reply_markup=markup)
    bot.register_next_step_handler(msg, process_photo_step)


@bot.message_handler(content_types=["photo", "document"])
def process_photo_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    if message.photo:
        user.photo = message.photo[-1]
        user.photo_id = message.photo[-1].file_id
    elif message.document and message.document.mime_type in ['image/jpeg', 'image/png']:
        user.document = message.document
        user.document_id = message.document.file_id

    else:
        msg = bot.reply_to(message, 'Это не фотография, пришлите пожалуйста фото.')
        bot.register_next_step_handler(msg, process_photo_step)

    msg = bot.send_message(message.chat.id, "Введите фамилию и имя")
    bot.register_next_step_handler(msg, process_fullname_step)


def process_fullname_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.fullname = message.text

    msg = bot.send_message(chat_id, '📅  Введите свой день месяц и год рождения! \n например: ДД.ММ.ГГГГ')
    bot.register_next_step_handler(msg, process_age_step)


cli_age = []


def process_age_step(message):
    pattern = re.compile(
        '(?<!\d)(?:0?[1-9]|[12][0-9]|3[01]).(?:0?[1-9]|1[0-2])(?!\d).(?:19[0-9][0-9]|20[01][0-9])(?!\d)', re.IGNORECASE)
    is_valid = pattern.match(message.text)
    if is_valid:
        cli_age.append(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.age = message.text

        msg = bot.send_message(chat_id, '📞  Ваш номер телефона:')
        bot.register_next_step_handler(msg, process_phone_step)
    else:
        msg = bot.reply_to(message, '😖  Вы ввели не правильную дату, попробуйте еще раз!')
        bot.register_next_step_handler(msg, process_age_step)


cli_phone = []


def process_phone_step(message):
    pattern = re.compile('^(\+)?\d+\D*\d{2}\D*\d{3}\D*\d{2}\D*\d{2}$', re.VERBOSE)
    is_valid = pattern.match(message.text.strip())
    if is_valid:
        cli_phone.append(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, '📧  Ваш email:')
        bot.register_next_step_handler(msg, process_email_step)

    else:
        msg = bot.reply_to(message, '😖  Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)


cli_mail = []  # Хранит в себе почту заявителя


def process_email_step(message):
    pattern = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)',
                         re.IGNORECASE)  # Проверяем совпадает ли паттерн
    is_valid = pattern.match(message.text)
    if is_valid:
        cli_mail.append(message.text)  # Записываем полученную почту

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.email = message.text

        msg = bot.send_message(chat_id, '🍏 Чем можете быть полезны клубу?')
        bot.register_next_step_handler(msg, process_effective_step)

    else:
        msg = bot.reply_to(message, '😖  Вы ввели что то другое. Пожалуйста введите корректный e-mail.')
        bot.register_next_step_handler(msg, process_email_step)


def process_effective_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.effective = message.text

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    ibtn1 = types.KeyboardButton('XJ')
    ibtn2 = types.KeyboardButton('XK')
    ibtn3 = types.KeyboardButton('XF')
    ibtn4 = types.KeyboardButton('S-Type')
    ibtn5 = types.KeyboardButton('X-Type')
    ibtn6 = types.KeyboardButton('F-Type')
    ibtn7 = types.KeyboardButton('XJ220')
    ibtn8 = types.KeyboardButton('XK8')
    ibtn9 = types.KeyboardButton('XE')
    ibtn10 = types.KeyboardButton('E-Type')
    ibtn11 = types.KeyboardButton('F-Pace')
    ibtn12 = types.KeyboardButton('E-Pace')
    ibtn13 = types.KeyboardButton('I-Pace')
    markup.add(ibtn1, ibtn2, ibtn3, ibtn4, ibtn5, ibtn6, ibtn7, ibtn8, ibtn9, ibtn10,
               ibtn11, ibtn12, ibtn13)

    msg = bot.send_message(chat_id, '🚘 Какая у вас модель Jaguar?:', reply_markup=markup)
    bot.register_next_step_handler(msg, process_carModel_step)


def process_carModel_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.carModel = message.text

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Бежевый')
    itembtn2 = types.KeyboardButton('Белый')
    itembtn3 = types.KeyboardButton('Голубой')
    itembtn4 = types.KeyboardButton('Желтый')
    itembtn5 = types.KeyboardButton('Зеленый')
    itembtn6 = types.KeyboardButton('Коричневый')
    itembtn7 = types.KeyboardButton('Красный')
    itembtn8 = types.KeyboardButton('Оранжевый')
    itembtn9 = types.KeyboardButton('Розовый')
    itembtn10 = types.KeyboardButton('Серый')
    itembtn11 = types.KeyboardButton('Синий')
    itembtn12 = types.KeyboardButton('Фиолетовый')
    itembtn13 = types.KeyboardButton('Черный')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10,
               itembtn11, itembtn12, itembtn13)

    msg = bot.send_message(chat_id, '🌈 Цвет автомобиля:', reply_markup=markup)
    bot.register_next_step_handler(msg, process_carColor_step)


def process_carColor_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.carColor = message.text

    msg = bot.send_message(chat_id, '🎰 Гос. номер автомобиля:')
    bot.register_next_step_handler(msg, process_carNumber_step)


def process_carNumber_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.carNumber = message.text

    msg = bot.send_message(chat_id, '🛢 Тип топлива:')
    bot.register_next_step_handler(msg, process_carFuel_step)


def process_carFuel_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.carFuel = message.text

    msg = bot.send_message(chat_id, '🍼 Объём двигателя (куб.см):')
    bot.register_next_step_handler(msg, process_engineVolume_step)


def process_engineVolume_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.engineVolume = message.text

        msg = bot.send_message(chat_id, '🗓 Год выпуска:')
        bot.register_next_step_handler(msg, process_carDate_step)

    except Exception as e:
        msg = bot.reply_to(message, 'Не тот объём товарищ! Введи исчо!')
        bot.register_next_step_handler(msg, process_engineVolume_step)


def process_carDate_step(message):
    int(message.text)
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.carDate = message.text

    # ваша заявка "Имя пользователя"
    # все ли правильно
    bot.send_message(chat_id, '📝 Проверьте все ли правильно!')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да ', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет ', callback_data='no')
    keyboard.add(key_no)
    bot.send_message(chat_id, getRegData(user, '🗿  Ваш ник нейм: '), parse_mode="Markdown")
    if user.document:
        bot.send_document(chat_id, caption='Ваше фото', data=user.document_id, reply_markup=keyboard)
    elif user.photo:
        bot.send_photo(chat_id, caption='Ваше фото', photo=user.photo_id, reply_markup=keyboard)



def getRegData(user, title):
    t = Template(
        book.Templ
    )
    return t.substitute({
        'title': title,
        'nickname': user.nickname,
        'userCity': user.city,
        'fullname': user.fullname,
        'age': user.age,
        'phone': user.phone,
        'email': user.email,
        'effective': user.effective,
        'carModel': user.carModel,
        'carColor': user.carColor,
        'carNumber': user.carNumber,
        'carFuel': user.carFuel,
        'engineVolume': user.engineVolume,
        'carDate': user.carDate

    })


@bot.callback_query_handler(func=lambda call: call.data in ["yes", "no"])  # теперь хэндлер принимает только yes и no
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Приятно познакомиться! Заявка принята! ")
        bot.send_message(call.message.chat.id, 'Добро пожалловать в ' + call.message.from_user.first_name,
                         reply_markup=rMenu)


    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Давайте попробуем еще раз! ")
        bot.send_message(call.message.chat.id, 'Напишите свой ник нейм: ')
        bot.register_next_step_handler(call.message, user_reg)
