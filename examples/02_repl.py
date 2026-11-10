from utils.llm import call_llm


def main():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    while True:
        # читаем сообщение пользователя из консоли
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            break

        # помещаем реплику пользователя в контекст
        messages.append({"role": "user", "content": user_input})

        # вызываем модель - она возвращает текстовое дополнение
        reply = call_llm(messages)

        # помещаем ответ модели в контекст
        messages.append({"role": "assistant", "content": reply})

        # показываем ответ в консоль
        print(reply)

    print(f"Контекст: {len(messages)} сообщений")


if __name__ == "__main__":
    main()
