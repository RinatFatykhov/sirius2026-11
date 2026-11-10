from utils.llm import call_llm


def main():
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]

    response = call_llm(messages)
    print(response)


if __name__ == '__main__':
    main()
