import telebot
from config import keys, TOKEN
from extensions import CryptoConvertor, ConvertionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def helper(message: telebot.types.Message):
    text = ('Ввод команд осуществлять через пробел, в следующем формате:\n<название валюты> \
<в какую валюту перевести> <количетсво валюты>\n Увидеть список всех доступных валют: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступны валюты: '
    for i in keys.keys():
        text = '\n'.join((text, i,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        length = message.text.split(' ')

        if len(length) != 3:
            raise ConvertionException('Необходимо ввести 3 параметра')

        quote, base, amount = length
        total = CryptoConvertor.get_price(quote, base, amount)
        total_base, course = total
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Курс {base}: {course}\nЦена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
