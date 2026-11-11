import os
# telebot — библиотека для работы с Telegram.
import telebot
from dotenv import load_dotenv


# Как создать своего тг-бота:
# 1. Откройте Telegram и введите в поиске @BotFather (убедитесь, что рядом с именем есть официальная синяя галочка верификации).
# 2. Нажмите кнопку Запустить или отправьте команду /start.
# 3. Отправьте команду /newbot.
# 4. Введите отображаемое имя бота (например: Мой Магазин Бот — его увидят пользователи).
# 5. Придумайте уникальный юзернейм (никнейм), по которому бота будут находить в поиске. Он должен заканчиваться на слово bot или _bot (например: my_super_shop_bot).
# 6. В ответ BotFather пришлет вам сообщение со ссылкой на бота и API-токен — секретный ключ для управления им (храните его в тайне!).
# 7. Добавьте строку в файл .env: TELEGRAM_BOT_TOKEN=<ваш-API-токен>

def main():
    # Подгружаем переменные из файла .env
    load_dotenv()

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
            "Начать новый диалог!"
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
            "Вы отправили мне: " + message.text
        )

    print("Бот запущен! Напишите ему в Telegram.")

    # Программа постоянно проверяет новые сообщения.
    # Она продолжает работать, пока мы её не остановим.
    bot.infinity_polling()

if __name__ == "__main__":
    main()