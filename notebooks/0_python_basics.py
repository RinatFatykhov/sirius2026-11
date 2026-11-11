import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Основы Python
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Числа

    ### int — целые числа
    """)
    return


@app.cell
def _():
    x = 5
    print(x)
    return


@app.cell
def _():
    a = 4 + 5
    b = 4 * 5
    c = 5 // 4
    d = 5 / 4
    e = 5**4
    f = 5 % 4
    g = (2 + 2) * 3
    print(a, b, c, d, e, f, g)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### float — дробные числа
    """)
    return


@app.cell
def _():
    y = 12.345
    print(y)
    return


@app.cell
def _():
    a_1 = 4.2 + 5.1
    b_1 = 4.2 * 5.1
    c_1 = 5.0 / 4.0
    d_1 = 5.25 // 4.25
    e_1 = 5.25 ** 4.0
    print(a_1, b_1, c_1, d_1, e_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Задание

    Посчитайте, чему равен x в выражении:

    $$x = \frac{2E}{A + 3C}$$

    - E = 12.8
    - A = 60
    - C = -13
    """)
    return


@app.cell
def _():
    # ваш код здесь

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Условия и циклы
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### if — условие
    """)
    return


@app.cell
def _():
    x_2 = 10

    if x_2 < 0:
        print('x отрицателен')

    if x_2 > 0:
        print('x положителен')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### while - цикл
    """)
    return


@app.cell
def _():
    x_3 = 0

    while x_3 < 10:
        x_3 = x_3 + 1
        print('x_3:', x_3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Задание

    посчитаем сумму всех чисел от 1 до 100 с помощью цикла

    s = 1 + 2 + 3 + ... + 100
    """)
    return


app._unparsable_cell(
    r"""
    i = 0
    s = 0

    while i < 100:
        i = i + 1
        # напишите сами
        s =

    print('Сумма:', s)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### for - цикл

    Сравните:

    ```python
    x_3 = 0

    while x_3 < 10:
        x_3 = x_3 + 1
        print('x_3:', x_3)
    ```
    """)
    return


@app.cell
def _():
    for x_5 in range(10):
        print('x_5:', x_5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Функции

    Функции нужны, чтобы не писать один и тот же кусок кода несколько раз
    """)
    return


@app.function
def compute_sum(n):
    s = 0
    for i in range(n + 1):
        s = s + i
    return s


@app.cell
def _():
    compute_sum(10)
    return


@app.cell
def _():
    compute_sum(100)
    return


@app.cell
def _():
    compute_sum(456)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Безымянная фунция _()

    Она полезна для того, чтобы мы не путали названия переменных

    Следующая ячейка не сработает, потому что переменная х уже объявлена в другой ячейке:
    """)
    return


@app.cell
def _():
    x = 10
    print(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    А так сработает, потому что здесь х используется только внутри функции
    """)
    return


@app.cell
def _():
    def _():
        x = 10
        return print(x)


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## str — строки
    """)
    return


@app.cell
def _():
    s_1 = 'это строка'
    s_2 = 'это тоже строка'

    print(s_1)
    print(s_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## list и dict - списки и словари
    """)
    return


@app.cell
def _():
    numbers = [1, 2, 3, 4]

    for num in numbers:
        print(num)
    return


@app.cell
def _():
    names = ['Alex', 'Kate', 'Bob']

    for name in names:
        print(name)
    return


@app.cell
def _():
    person = {'name': 'Bob', 'age': 44}

    print(person['name'])
    print(person['age'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Пример сложной структуры
    """)
    return


@app.cell
def _():
    people = [
        {'name': 'Alex', 'age': 14},
        {'name': 'Kate', 'age': 30},
        {'name': 'Bob', 'age': 44},
    ]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Задание

    Для каждого человека из people выведите его имя и возраст
    """)
    return


@app.cell
def _():
    # ваш код здесь

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Вызов LLM
    """)
    return


@app.cell
def _():
    from utils.llm import call_llm

    return (call_llm,)


@app.cell
def _(call_llm):
    def _():
        messages = [
            {"role": "user", "content": "Сколько будет 15 + 15?"}
        ]

        response = call_llm(messages)
        return print(response)


    _()
    return


@app.cell
def _(call_llm):
    def _():
        messages = [
            {"role": "user", "content": "Сколько будет 15 + 15? Напиши только число."}
        ]

        response = call_llm(messages)
        return print(response)


    _()
    return


@app.cell
def _(call_llm):
    def _():
        messages = [
            {"role": "user", "content": "Сколько будет 15 + 15?"},
            {"role": "assistant", "content": "30"},
            {"role": "user", "content": "Спасибо"},
        ]

        response = call_llm(messages)
        return print(response)


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Мы можем подставить в историю **что угодно**!
    """)
    return


@app.cell
def _(call_llm):
    def _():
        messages = [
            {"role": "user", "content": "Сколько будет 15 + 15?"},
            {"role": "assistant", "content": "40"},
            {"role": "user", "content": "Спасибо"},
        ]

        response = call_llm(messages)
        return print(response)


    _()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
