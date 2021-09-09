from telebot import types
import book, btn, regg, sell_form


user_dict = regg.user_dict


class User:
    def __init__(self, nickname, photo, document):
        self.nickname = nickname
        self.photo = photo
        self.document = document

        for key in keys:
            self.key = None

#bot = telebot.TeleBot(config.TOKEN)
bot = regg.bot
#hello_count = []

#START
@bot.message_handler(commands=['start'])
def start_message(message):
    #if len(hello_count) == 0:  # Проверяем здоровались ли мы ранее
    bot.send_sticker(message.chat.id, book.sticker)
    bot.send_message(message.chat.id, message.from_user.first_name + book.hello)
    bot.send_message(message.chat.id, book.lang, reply_markup=keyboard1)

#МЕНЮ ВЫБОРА ЯЗЫКА
keyboard1 = types.ReplyKeyboardMarkup(True)
keyboard1.row(book.eng, book.rus)

#РУССКОЕ МЕНЮ
rMenu = btn.russian_menu
#АНГЛИЙСКОЕ МЕНЮ
eMenu = btn.english_menu

@bot.message_handler(content_types=['text'])
def send_text(message):
    #Выбор языка
    if message.text == '🇬🇧 English':
        bot.send_message(message.chat.id, book.lang_eng, reply_markup=eMenu)
        bot.send_message(message.chat.id, book.check)
    elif message.text == '🇷🇺 Русский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_reg = types.KeyboardButton(book.btnreg)
        btn_noAuto = types.KeyboardButton(book.btnNoaut)
        markup.add(btn_reg, btn_noAuto)
        bot.send_message(message.chat.id, book.lang_rus)
        bot.send_message(message.chat.id, book.reg, reply_markup=markup)

    elif message.text == 'У меня пока нет авто':
        bot.send_message(message.chat.id, book.advice, reply_markup=btn.Our_communit)

    # Начало регистрации англ
    elif message.text == '/check':
        bot.send_message(message.from_user.id, str(message.from_user.username) + book.ms_engl) # дальше этого не будетб будет все иначе
        bot.register_next_step_handler(message, regg)
    #Возврат в главное меню
    elif message.text == '🔙 Главное меню':
        bot.send_message(message.chat.id, book.msMenu_back, reply_markup=rMenu)
    #Возврат в главное меню англ
    elif message.text == '🔙 Main menu':
        bot.send_message(message.chat.id, book.msMenu_backEn, reply_markup=eMenu)

    #Русское меню
    elif message.text == '🚗 Мой профиль':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        bot.send_message(message.chat.id, regg.getRegData(user, '🗿  Ваш ник нейм: '), parse_mode="Markdown")
        if user.document:
            bot.send_document(chat_id, caption='Ваше фото', data=user.document_id)
        elif user.photo:
            bot.send_photo(chat_id, caption='Ваше фото', photo=user.photo_id)



    elif message.text == '🛒 Маркет':
        bot.send_sticker(message.chat.id, book.sticker6)
        bot.send_message(message.chat.id, book.market, reply_markup=btn.market)
    elif message.text == '🚗 Продать авто':
        bot.send_sticker(message.chat.id, book.sticker6)
        bot.send_message(message.chat.id, sell_form.s)
    elif message.text == '📰 Новости':
        bot.send_sticker(message.chat.id, book.sticker1)
        bot.send_message(message.chat.id, book.news)
        bot.send_message(message.chat.id, '👥 Наши мероприятия: ', reply_markup=btn.fak_otdyh)
    elif message.text == '⚙ Настройки':
        bot.send_sticker(message.chat.id, book.sticker2)
        bot.send_message(message.chat.id, book.settingCh, reply_markup=btn.tuning)
    elif message.text == '👥 Наши сообщества':
        bot.send_sticker(message.chat.id, book.sticker3)
        bot.send_message(message.chat.id, book.cha, reply_markup=btn.Our_communities)
    elif message.text == '➕ Пригласить нового участника':
        bot.send_sticker(message.chat.id, book.sticker3)
        bot.send_message(message.chat.id, book.unique_link)


    #Отдых
    elif message.text == '☑️ Отдых':
        bot.send_message(message.chat.id, '👥 Наши мероприятия:', reply_markup=btn.fak_otdyh)
    #Английское меню

    elif message.text == '👳🏽‍♂️ About Us':
        bot.send_sticker(message.chat.id, book.sticker4)
        bot.send_message(message.chat.id, book.abt)
        bot.send_message(message.chat.id, book.ab, reply_markup=btn.about)
    elif message.text == '📰 News':
        bot.send_sticker(message.chat.id, book.sticker1)
        bot.send_message(message.chat.id, book.news_engl)


btnFuck = btn.fakmenu  # Кнопки ФАК, форум, маркет
reg_button = btn.reg_button  # кнока рег
sell_auto = sell_form.s # форма заявки продажи авто


# Разрешить сохранение обработчиков следующего шага в файл "./.handlers-saves/step.save".
# Delay = 2 означает, что после любого изменения в обработчиках следующего шага (например, вызов register_next_step_handler ())
# сохранение произойдет после задержки в 2 секунды.
bot.enable_save_next_step_handlers(delay=2)

# Загрузить next_step_handlers из файла сохранения (по умолчанию "./.handlers-saves/step.save")
# ВНИМАНИЕ! Это будет работать, только если был вызван enable_save_next_step_handlers!
bot.load_next_step_handlers()


#row_count = sheet_active.max_row #Получили количество строк на странице
#column_count = sheet_active.max_column #Получили количество колонок на странице
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

# RUN
bot.polling(none_stop=True)