from telebot import types


#русское меню
russian_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
russian_menu.row('🚗 Мой профиль', '🛒 Маркет', '🔧 СТО', '📰 Новости')
russian_menu.row('👥 Наши сообщества', '➕ Пригласить нового участника', '⚙ Настройки')

# Английское меню
english_menu = types.ReplyKeyboardMarkup(True)
english_menu.row('🚗 My cars', '🛒 Market', '🔧 Car service', '📰 News')
english_menu.row('👥 Our partners', '➕ Invite a new member', '⚙ Settings')

# маркет
market = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
market.row('🚗 Продать авто', '📝 Объявления о продаже', '🔩 Запчасти')
market.row('🔙 Главное меню')

#МЕНЮ кнопки Настройки ЯЗЫК ru
tuning = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton('🚗 Автомобиль', callback_data='auto')
item2 = types.InlineKeyboardButton('🏙 Город', callback_data='city')
item3 = types.InlineKeyboardButton(text='👄 Изменить язык', callback_data='lang')
item4 = types.InlineKeyboardButton(text='🚹 Никнейм ', callback_data='nickname')
item5 = types.InlineKeyboardButton('🖼 Изменить фото машины', callback_data='photo')
item6 = types.InlineKeyboardButton('🗣⁉️ Частые вопросы', callback_data='fak')
tuning.add(item1, item2, item3, item4, item5, item6)

#МЕНЮ кнопки Настройки ЯЗЫК en
about = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton('🚗 Car', callback_data='Car')
item2 = types.InlineKeyboardButton('🏙 Change city', callback_data='city')
item3 = types.InlineKeyboardButton('👄 Choose language', callback_data='start')
item4 = types.InlineKeyboardButton('⁉️ FAQ', callback_data='faq')
about.add(item1, item2, item3, item4)

#кнопки наши сообщества
Our_communities = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton('🦁  Jaguar Club Belarus чат', url='https://t.me/jaguarclubbelarus')
item2 = types.InlineKeyboardButton('💭  Jaguar Club Belarus Флудильня ', url='https://t.me/jcb_chat')
item3 = types.InlineKeyboardButton('🐈  Jaguar Club JFC ', url='https://t.me/jaguar_club_jfc')
item4 = types.InlineKeyboardButton('🏪  Jaguar Club JFC маркет', url='https://t.me/Market_JFC')
Our_communities.add(item1, item2, item3, item4)

#кнопки сообщества к кнопке у меня нет пока авто
Our_communit = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton('👨‍👨‍👧‍👧  Jaguar Club Belarus чат', url='https://t.me/jaguarclubbelarus')
item2 = types.InlineKeyboardButton('💭  Jaguar Club Belarus Флудильня ', url='https://t.me/jcb_chat')

Our_communit.add(item1, item2)

# кнопка рег
reg_button = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton('/reg')
reg_button.add(item1)

# Кнопки отдых меропрития пожертвовать
fak_otdyh = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton('🔓 Открытие сезона 2021 ', url='https://jaguarclubbelarus.by')
item2 = types.InlineKeyboardButton('☕️ Вечерние посиделки', url='https://t.me/jcb_chat')
item3 = types.InlineKeyboardButton('💸 Пожертвовать на развите клуба', url='https://t.me/ultravioletpartyeyes')
fak_otdyh.add(item1, item2, item3)

# Кнопки ФАК, форум, маркет
fakmenu = types.ReplyKeyboardMarkup(True)
fakmenu.row('☑️ ФАК')
fakmenu.row('☑️ Форум ', '☑️ Маркет')
fakmenu.row('🔙 Главное меню')

