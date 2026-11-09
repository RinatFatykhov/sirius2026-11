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
    ### int — целые числа
    """)
    return


@app.cell
def _():
    x = 5
    print(x, '|', type(x))
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
    **Задание:** x = 3, y = -1. Чему равно выражение?
    """)
    return


@app.cell
def _():
    # your code here
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
    print(y, '|', type(y))
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


@app.cell
def _():
    a_2 = 5
    print(a_2, '|', type(a_2))
    a_2 = float(a_2)
    print(a_2, '|', type(a_2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### bool — True / False
    """)
    return


@app.cell
def _():
    a_3 = True
    b_2 = False
    print(a_3, '|', type(a_3))
    print(b_2, '|', type(b_2))
    return a_3, b_2


@app.cell
def _(a_3, b_2):
    print(a_3 + b_2)
    print(a_3 + a_3)
    print(b_2 + b_2)
    return


@app.cell
def _(a_3, b_2):
    print(int(a_3), int(b_2))
    return


@app.cell
def _():
    print(True and False)
    print(True or True)
    print(not False)
    return


@app.cell
def _():
    a_4 = 2 == 3
    b_3 = 4 < 5
    print(a_4, '|', type(a_4))
    print(b_3, '|', type(b_3))
    return a_4, b_3


@app.cell
def _(a_4, b_3):
    a_4 or (a_4 and (not b_3))
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
    elif x_2 == 0:
        print('x равен нулю')
    else:
        print('x положителен')
    print('Done')
    return (x_2,)


@app.cell
def _(x_2):
    if x_2 > 3 and x_2 < 11 or x_2 == 5:
        print(x_2)
        print('nice')
    return


@app.cell
def _():
    x_3 = 3
    y_1 = 5
    if x_3 == 3:
        if y_1 > 6:
            print('y greater than 6')
        else:
            print('y not grater than 6')
        print('x is equal to 3')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### None — ничего
    """)
    return


@app.cell
def _():
    z = None
    print(z, '|', type(z))
    return (z,)


@app.cell
def _(z):
    if z is None:
        z_1 = 'I am None!'
    z_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### str — строки
    """)
    return


@app.cell
def _():
    x_4 = 'abc'
    y_2 = 'xyz'
    print(x_4, '|', type(x_4))
    print(y_2, '|', type(y_2))
    return


@app.cell
def _():
    a_5 = 'Андрей'
    b_4 = 'Михайлович'
    s = a_5 + ' ' + b_4
    print(s)
    return (a_5,)


@app.cell
def _(a_5):
    print(a_5.upper())
    print(a_5.lower())
    return


@app.cell
def _(a_5):
    print(len(a_5))
    return


@app.cell
def _(a_5):
    print(a_5)
    print(a_5[0])
    print(a_5[1])
    return


@app.cell
def _(a_5):
    i = 0
    j = 4
    print(a_5[i:j])
    return


@app.cell
def _():
    s_1 = 'ya stroka'
    if 'ya' in s_1:
        print("ya deistvitel'no stroka")
    return


@app.cell
def _():
    splitted_line = "Райгородский Андрей Михайлович".split()
    print(splitted_line)
    return


@app.cell
def _():
    splitted_line_1 = 'Райгородский Андрей Михайлович'.split('р')
    print(splitted_line_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### list — список
    """)
    return


@app.cell
def _():
    a_6 = list()
    b_5 = []
    print(a_6 == b_5)
    return


@app.cell
def _():
    c_2 = [2, 'a', [4, 'stroka', 6.56]]
    return (c_2,)


@app.cell
def _(c_2):
    c_2.append(4.67)
    c_2
    return


@app.cell
def _(c_2):
    c_2.pop()
    c_2
    return


@app.cell
def _(c_2):
    print(c_2[0])
    print(c_2[2])
    print(c_2[-1])
    return


@app.cell
def _(c_2):
    d_2 = c_2[1:3]
    print(d_2)
    return


@app.cell
def _(c_2):
    c_2.index('a')
    return


@app.cell
def _(c_2):
    5 in c_2
    return


@app.cell
def _(c_2):
    if 'a' in c_2:
        print("element 'a' in c")
    return


@app.cell
def _():
    c_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d_3 = c_3[1:7:2]
    print(d_3)
    return (c_3,)


@app.cell
def _(c_3):
    print(c_3)
    d_4 = c_3[::-1]
    print(d_4)
    return


@app.cell
def _(c_3):
    print(c_3)
    c_3[0] = 100500
    print(c_3)
    return


@app.cell
def _(c_3):
    c_3[2:5] = [80]
    print(c_3)
    c_3[2:5] = [80, 90]
    print(c_3)
    return


@app.cell
def _(c_3):
    d_5 = [9, 0]
    c_3 + d_5
    return (d_5,)


@app.cell
def _(c_3, d_5):
    c_3 - d_5
    return


@app.cell
def _(c_3):
    len(c_3)
    return


@app.cell
def _(c_3):
    c_3.sort()
    c_3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Задание 1
    Проверьте, является ли x строкой. Если в ней больше одного слова — выведите их количество и слова по алфавиту
    """)
    return


@app.cell
def _():
    # your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Задание 2
    Переверните элементы списка x с нечётными индексами
    """)
    return


@app.cell
def _():
    # your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### tuple — кортеж (неизменяемый)
    """)
    return


@app.cell
def _():
    t = 'a', 5, 12.345, (2, 'b')
    t
    return (t,)


@app.cell
def _(t):
    print(t[2])
    print(t.index(5))
    print(t[:2])
    return


@app.cell
def _(t):
    m = (1, 2, 3)
    print(t + m)
    print(len(t))
    print(5 in t)
    return


@app.cell
def _():
    a_7 = [1, 2, 3]
    b_6 = a_7
    b_6[0] = 49
    print(a_7)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Циклы: for и while
    """)
    return


@app.cell
def _():
    models = ['decision tree', 'linear model', 'svm', 'ensemble']
    for model in models:
        print(model)
    print("Done")
    print(model)
    return


@app.cell
def _():
    x_5 = 1
    while x_5 <= 10:
        print(x_5)
        x_5 = x_5 + 1
    return


@app.cell
def _():
    mas = ['stroka1', 'stroka2', 'stroka3', 'stop', 'stroka4']
    for s_3 in mas:
        if s_3 == 'stop':
            break
        print(s_3)
    return


@app.cell
def _():
    mas_1 = ['stroka1', 'null', 'stroka3', 'stop', 'null']
    for s_4 in mas_1:
        if s_4 == 'null':
            continue
        print(s_4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### range
    """)
    return


@app.cell
def _():
    r = range(1, 100, 10)
    print(list(r))
    return


@app.cell
def _():
    for i_1 in range(1, 10, 1):
        print(i_1)
    return


@app.cell
def _():
    list(range(4, 8))
    return


@app.cell
def _():
    list(range(8))
    return


@app.cell
def _():
    models_1 = ['decision tree', 'linear model', 'svm', 'ensemble']
    for i_2 in range(len(models_1)):
        print(models_1[i_2])
    print('Done')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Задание 3
    Выведите числа от 0 до 500, которые делятся на 7 и содержат цифру 8
    """)
    return


@app.cell
def _():
    # your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### zip и enumerate
    """)
    return


@app.cell
def _():
    first = 'a b c d e f g'.split(' ')
    second = '1 2 3 4 5 6 7'.split(' ')
    list(zip(first, second))
    return


@app.cell
def _():
    first_1 = 'a b c d e f g'.split(' ')
    second_1 = '1 2 3 4 5'.split(' ')
    list(zip(first_1, second_1))
    return


@app.cell
def _():
    models_2 = ['decision tree', 'linear model', 'svm', 'ensemble']
    for num, model_1 in zip(range(len(models_2)), models_2):
        print(str(num + 1) + "'s model is:", model_1)
    return


@app.cell
def _():
    models_3 = ['decision tree', 'linear model', 'svm', 'ensemble']
    for num_1, model_2 in enumerate(models_3):
        print(str(num_1 + 1) + "'s model is:", model_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Задание 4
    Создайте списки a и b, выведите нумерованные пары их элементов
    """)
    return


@app.cell
def _():
    # Ваш код здесь
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### set — множество
    """)
    return


@app.cell
def _():
    s_5 = set()
    print(s_5, '|', type(s_5))
    return


@app.cell
def _():
    s_6 = set([5, 2, 3, 2])
    s_6
    return (s_6,)


@app.cell
def _(s_6):
    s_6.add(1)
    s_6.add('a')
    s_6.add(None)
    s_6.add('bullet')
    print(s_6)
    return


@app.cell
def _():
    s1 = set(range(0, 10))
    s2 = set(range(5, 15))
    print('s1: ', s1, '\ns2: ', s2)
    return s1, s2


@app.cell
def _(s1, s2):
    print(s1.difference(s2))
    print()
    print(s2.difference(s1))
    return


@app.cell
def _(s1, s2):
    print(s1.intersection(s2))
    print(s1 & s2)
    return


@app.cell
def _(s1, s2):
    print(s1.union(s2))
    print(s1 | s2)
    return


@app.cell
def _(s1):
    s1.discard(0)
    s1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### dict — словарь
    """)
    return


@app.cell
def _():
    d_6 = {}
    dd = dict()
    print(d_6 == dd, '|', type(d_6))
    return (d_6,)


@app.cell
def _(d_6):
    key = 'a'
    value = 100
    d_6[key] = value
    d_6
    return


@app.cell
def _():
    d_7 = {'short': ['dict'], 'long': 'dictionary'}
    d_7
    return


@app.cell
def _():
    d_8 = dict(short='dict', long='dictionary')
    d_8
    return


@app.cell
def _():
    d_9 = dict([(1, 1), (2, 4)])
    d_9
    return


@app.cell
def _():
    d_10 = dict.fromkeys(['a', 'b'])
    d_10
    return


@app.cell
def _():
    d_11 = dict.fromkeys(['a', 'b'], 100)
    d_11
    return (d_11,)


@app.cell
def _(d_11):
    100 in d_11
    return


@app.cell
def _():
    d_12 = {a: a ** 2 for a in range(7)}
    d_12
    return


@app.cell
def _():
    d_13 = {1: 100, 2: 200, 3: 300}
    d_13['a']
    return (d_13,)


@app.cell
def _(d_13):
    d_13.get(1)
    return


@app.cell
def _(d_13):
    d_13.get('a') == None
    return


@app.cell
def _(d_13):
    print(list(d_13.keys()))
    return


@app.cell
def _(d_13):
    print(list(d_13.values()))
    return


@app.cell
def _(d_13):
    print(list(d_13.items()))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Задание 5
    Одной строкой: словарь, где каждой строке из mas соответствует пара (индекс, длина)
    """)
    return


@app.cell
def _():
    # Ваш код здесь
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Функции
    """)
    return


@app.cell
def _():
    def f_1(x):
        return x ** 2

    def mlt_f(a, b, c=0):
        if c > 0:
            return a + b
        return a - b
    (f_1(3), mlt_f(3, 2))
    return


@app.cell
def _():
    g_1 = lambda x: x ** 2
    g_1(3)
    return


@app.cell
def _():
    l_1 = [2, 3, 4, 1, 0, -10, 5, 6, 100]
    sorted(l_1)
    return (l_1,)


@app.cell
def _(l_1):
    def f_2(x):
        return abs(x)
    sorted(l_1, key=f_2)
    return


@app.cell
def _(l_1):
    sorted(l_1, key=lambda x: abs(x))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Модули
    """)
    return


@app.cell
def _():
    import collections

    return


@app.cell
def _():
    from collections import Counter

    return


@app.cell
def _():
    import collections as cool_lib

    return (cool_lib,)


@app.cell
def _(cool_lib):
    count = cool_lib.Counter()
    return


@app.cell
def _():
    import numpy as np

    return


if __name__ == "__main__":
    app.run()
