import telebot
from telebot import types
from telebot.types import Message

# @Knowmoreee_bot

token = ("")

bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def send_message(message: Message):
    bot.send_message(message.chat.id, "salom dar in bot shumo metavoned dar borai sot setyho va messengerho malumot gired")
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Telegram")
    btn2 = types.KeyboardButton("Whatsapp")
    btn3 = types.KeyboardButton("Instagram")
    btn4 = types.KeyboardButton("YouTube")
    btn5 = types.KeyboardButton("Twiter")
    btn6 = types.KeyboardButton("Skype")
    btn7 = types.KeyboardButton("TikTok")
    btn8 = types.KeyboardButton("Facebook")
    btn9 = types.KeyboardButton("Vk")
    btn10 = types.KeyboardButton("Ok")


    markup.add(btn1,btn10,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
    bot.send_message(message.chat.id, "sot sety yo messengero intikhob namoed", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def send_message(message):
    if message.text == "Telegram":
        with open("telegram.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Telegram от др.-греч. τῆλε — далеко и γράμμα — запись) — кроссплатформенный мессенджер. Основан в 2013 году Павлом и Николаем Дуров")
        
    elif message.text == "Whatsapp":
        with open("whatsapp.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "WhatsApp (официально WhatsApp Messenger) — американский бесплатный сервис обмена мгновенными сообщениями (IM) и голосовой связи по IP (VoIP), принадлежащий компании Meta. Позволяет пользователям обмениваться текстовыми и голосовыми сообщениями, совершать голосовые и видеозвонки, обмениваться изображениями, документами, местоположением пользователя и другими данными. Для регистрации требует[2] указания номера мобильного телефона.")
    elif message.text == "Instagram":
        with open("instagram.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"Instagram (рус. Инстагра́м) — американская социальная сеть для обмена фотографиями и видео, основанная Кевином Систромом и Майком Кригером. В апреле 2012 года компания Facebook Inc. (ныне Meta) приобрела сервис за ~1 миллиард долларов США наличными и акциями. Приложение позволяет пользователям загружать медиафайлы, которые можно редактировать с помощью фильтров и организовывать с помощью хештегов и географических меток. Сообщениями можно делиться публично или с заранее одобренными подписчиками. Пользователи могут просматривать контент других пользователей по тегам и местоположению, а также просматривать трендовые материалы. Пользователи могут лайкать фотографии и подписываться на других пользователей, чтобы добавить их контент в личную ленту")
    
    elif message.text == "YouTube":
        with open("yt.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"YouTube (МФА: [ˈjuːt(j)uːb], юту́б, ютью́б) — американский видеохостинг, основанный в 2005 году. С октября 2006 года принадлежит компании Google. YouTube стал популярнейшим видеохостингом и вторым сайтом в мире по количеству посетителей. На 2020 год у него более 2,5 млрд ежемесячных пользователей, которые ежедневно просматривают более 1 млрд часов видео[11]. На 2021 год на сервисе насчитывалось, в общей сложности, около 14 млрд видеороликов.")
    elif message.text == "Twiter":
        with open("twiter.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"«Тви́ттер» (англ. Twitter), в процессе ребрендинга в X, — американская социальная сеть. Это пятый по посещаемости сайт в мире и одна из крупнейших социальных сетей с 550 млн пользователей ежемесячно")
    elif message.text == "Skype":
        with open("skype.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"Skype (МФА: [skaɪ̯p]) — бесплатное проприетарное программное обеспечение с закрытым кодом, обеспечивающее текстовую, голосовую и видеосвязь через Интернет между компьютерами (IP-телефония), опционально используя технологии пиринговых сетей, а также платные услуги для звонков на мобильные и стационарные телефоны. По состоянию на конец 2010 года у программы было 663 млн пользователей Skype используют 40 миллионов активных пользователей в день. Большинство разработчиков и 44 % работников общего отдела находится в Эстонии — Таллине и Тарту")
    elif message.text == "TikTok":
        with open("tiktok.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"TikTok («ТикТок») — сервис для создания и просмотра коротких видео, принадлежащий пекинской компании «ByteDance». Запущенная в 2018 году международная версия является ведущей видеоплатформой для коротких видео в Китае и становится всё более популярной в других странах, став одним из наиболее быстрорастущих и скачиваемых приложений")
    elif message.text == "Facebook":
        with open("facebook.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"Facebook («Фе́йсбу́к», [ˈfeɪsˌbʊk]) — крупнейшая социальная сеть в мире, которой владеет компания Meta Platforms (до 28 октября 2021 года — Facebook Inc.). Была основана 4 февраля 2004 года Марком Цукербергом и его соседями по комнате во время обучения в Гарвардском университете — Эдуардо Саверином, Дастином Московицем и Крисом Хьюзом.")
    elif message.text == "Vk":
        with open("vk.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"«ВКонта́кте» (международное название — VK) — российская социальная сеть со штаб-квартирой в Санкт-Петербурге. Запущена в 2006 году Павлом Дуровым.")
    elif message.text == "Ok":
        with open("ok.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"«Однокла́ссники» (OK.ru) — российская социальная сеть, принадлежащая VK. На май 2022 года 50-й по популярности сайт в мире. Проект запущен 26 марта 2006 года.")



bot.polling()

