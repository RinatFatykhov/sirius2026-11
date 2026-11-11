import os
# telebot — библиотека для работы с Telegram.
import telebot

# Получаем секретный токен из переменной окружения.
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Не задан TELEGRAM_BOT_TOKEN")

# Создаём объект бота.
bot = telebot.TeleBot(TOKEN)


# Эта функция срабатывает при команде /new.
@bot.message_handler(commands=["new"])
def new_chat(message):
    bot.send_message(
        message.chat.id,
        "Новая сессия начата!"
    )


# Эта функция срабатывает, когда присылают фотографию.
@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    bot.send_message(
        message.chat.id,
        "Это картинка 🖼️"
    )


# Эта функция срабатывает на обычные текстовые сообщения.
@bot.message_handler(content_types=["text"])
def echo(message):
    # message.text — текст, который прислал пользователь.
    # message.chat.id — идентификатор чата для ответа.
    bot.send_message(
        message.chat.id,
        message.text
    )


print("Бот запущен! Напишите ему в Telegram.")

# Программа постоянно проверяет новые сообщения.
# Она продолжает работать, пока мы её не остановим.
bot.infinity_polling()
