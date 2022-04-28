from telebot import types


hello = ' ✌🏻Hello! My name is Bot Cat'
lang = '🇬🇧🇷🇺Please select a language'

eng = '🇬🇧 English'
rus = '🇷🇺 Русский'

# Стикеры
sticker = 'CAACAgIAAxkBAAEBUXNgpo1rA5eufv4NzUV-a_uB_AmIcgACGQAD6dgTKFdhEtpsYKrLHwQ'
sticker1 = 'CAACAgIAAxkBAAEBUX9gpqjNVd7qVhlffiUBFyxZvvEnlgACDgAD6dgTKBOmPUNf-EgfHwQ'
sticker2 = 'CAACAgIAAxkBAAEBUXxgppNqNyzEfl_pZudmUHvuUAg11gACGAAD6dgTKPjpR-x-G745HwQ'
sticker3 = 'CAACAgIAAxkBAAEBXb1gtLeBOpEqSizdwW0GrRkUmm8H8AACCgAD6dgTKGnSgBkGwWd-HwQ'
sticker4 = 'CAACAgIAAxkBAALgO17LqZloNFUU-m_JFtgIInPnleiYAAIzAANMH-oXJQkZ9WAV6soZBA'
sticker5 = 'CAACAgIAAxkBAAEBdjdgzl06PouQWTfwsTfMysF34GlGrgACCgAD6dgTKGnSgBkGwWd-HwQ'
sticker6 = 'CAACAgIAAxkBAAEBealg0mVsNM4o78UEjq0Qvo8gBRAYwQACBAAD6dgTKI-N1iBvaYiZHwQ'
sticker7 = 'CAACAgIAAxkBAAECoMtgFtfzmyQGLLaZtlg6Qasmb90cwACdQ8AAr0nEUoDQnRWf0YLYSAE'

# Гиф анимация
gifAnim = 'CgACAgQAAxkBAAEBfcVg1zs09URk-FTBg9QlM-tRO3tmvAACigIAAqA0nVLdEFOHRVGPXiAE'


# Новости на англ
news_engl = ('Our partners report:' + '\n' +
                         'Installment for 5 MONTHS on the HALVA card in ML-auto.by for all goods for any order amount!' + '\n' + 'Our managers will help you with the selection. '+' \n'+
                         '📱 Call +375447098731 A1 and Viber, +375298712433 MTC' + '\n' +
                         'And our partner service stations will help you with the repair and maintenance of your cars:' + '\n' +
                         '🔥 STO AutoGilService, Minsk, Matusevich str., 33 building 7 +375444681948 A1 and Viber, +375298381948 MTC www.autogil.by' + '\n' +
                         '🔥 STO MLavtoservice - Minsk, Platonova str. 14B, +375445639080 A1 and Viber, +375333539080 MTC www.ml-autoservice.by' + '\n' +
                         'Now you can service your car with high quality and at a discount, provided that you buy goods on ML-auto.by' + '\n' +
                         '👍👍👍 At our service stations you can pay for services by installment cards.')
# О нас
abt = 'Company - Delivery of goods from BAD_MINT'
ab = 'Our company BAD_MINT was founded in 2021, '\
                                          'we are engaged in the development of websites,'\
                                          ' mobile applications, bots in telegrams '

# Английский
lang_eng = '🇬🇧 Your language is English'
check = 'To register in the club enter 👉 /check'
ms_engl = ' Write your nickname: '
msMenu_backEn ='🤔 You are returned to the main menu. What are we going to do next? '

# Английское меню
english_menu = types.ReplyKeyboardMarkup(True)
english_menu.row('🚗 My cars', '🛒 Market', '📰 News')
english_menu.row('👥 Our partners', '➕ Invite a new member', '⚙ Settings')

#русскй
lang_rus = '🇷🇺 Ваш язык Русский'
btnNoaut = 'У меня пока нет авто'
reg = 'Чтобы зарегистрироваться в клубе введите 👉 /reg'
btnreg = '/reg'
advice = '👣  Перейти в клубный чат телеграм спросить совет! : '
mReg = 'У вас пока нет зарегестрированных машин, пройдите регистрацию введите "/reg" '
ms = ' Напишите свой ник нейм: '
msMenu_back = '🤔 Вы вернулись в главное меню. Чем займемся дальше?'
during = 'В процессе разработки'
settingCh = 'В настройках вы можете изменить:'
cha = '💬 Чаты нашего клуба и наших друзей:'
regCity = '🌃 Ваш город?:'
regCity1 = '🤓 Если НЕТ такого в списке введите в ручную!'
market = '😁 Товар лицом продавай, а покупателя не надувай! \n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖ \n👇 Сделайте свой выбор:'
unique_link = '🔗 Ваша уникальная ссылка для приглашения друга:' + '\n' + '  ' + '\n' +\
              '⤵️ ⤵️ ⤵️' + '\n' + '  ' + '\n' + '@JaguarClubBelarus_bot'
sto = 'Ремонт Jaguar/Land Rover в минске. Опыт работы только в этом направлении 9 лет подряд.\n' \
      'На данный момент есть возможность выполнения следующих услуг: замена тормозных.дисков/колодок,\n' \
      'переборка тормозных.суппортов,диагностика подвески, выполнение ТО.замена ремней грм и тнвд.\n' \
      'Есть возможность поднятия кузова и дальнейшая обработка антикоррозийными составами(все на месте,подняли,обработали,опустили) и т.д.\n' \
      'по цене лучше сориентироваться при звонке. Индивидуальный подход к каждому клиенту.\n' \
      'Сделаю дешевле чем у качественных конкурентов в этом направлении в минске,гарантирую) +375293154040'


#русское меню
russian_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
russian_menu.row('🚗 Мой профиль', '🛒 Маркет', '🔧 СТО', '📰 Новости')
russian_menu.row('👥 Наши сообщества', '➕ Пригласить нового участника', '⚙ Настройки')


#Новости
news = ('Наши партнеры сообщают:' + '\n' +
                         'Рассрочка на 5 МЕСЯЦЕВ по карте ХАЛВА в ML-auto.by на все товары при любой сумме заказа! Наши менеджеры помогут с подбором.'+'\n'+
                         '📱 Звоните +375447098731 A1 и Viber, +375298712433 MTC' + '\n' +
                         ' А помогут с ремонтом и обслуживанием Ваших авто наши партнерские СТО:' + '\n' +
                         '🔥 СТО АвтоГилСервис, г.Минск, ул.Матусевича д.33 к.7 +375444681948 A1 и Viber, +375298381948 MTC www.autogil.by' + '\n' +
                         '🔥 СТО МЛавтосервис - г.Минск ул.Платонова 14Б, +375445639080 A1 и Viber, +375333539080 MTC www.ml-autoservice.by' + '\n' +
                         'Теперь можно качественно и со скидкой обслужить свой автомобиль на наших СТО при условии покупки товаров на ML-auto.by' + '\n' +
                         '👍👍👍 На наших СТО можно оплачивать услуги картами рассрочек')

# карточка участника по окончании регистрации
Templ = '$title  *$nickname* \n 🌇 Город: *$userCity* ' \
        '\n 👥  ФИО: *$fullname* \n 🗓  Ваш день рождения:  *$age* ' \
        '\n 📞  Телефон: *$phone* \n 📧  Ваш email: *$email* ' \
        '\n 🍏  Чем можете быть полезным для клуба: *$effective* ' \
        '\n 🚘  Модель Jaguar: *$carModel* \n 🌈  Цвет автомобиля: *$carColor* ' \
        '\n 🎰  Гос. номер автомобиля: *$carNumber* \n 🛢 Тип топлива: *$carFuel*' \
        '\n 🍼 Объём двигателя: *$engineVolume* \n 🗓  Год выпуска: *$carDate* '


# Ключи для карточки участника при регистрации
keyReg = ['nickname', 'userCity', 'fullname', 'age', 'phone', 'effective', 'email'
                'carModel', 'carColor', 'carNumber', 'carFuel', 'engineVolume', 'carDate']


