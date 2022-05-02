"""Реализовать функцию get_jokes(), возвращающую n шуток
сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:

["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?"""

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes2 = []


def get_jokes(n, flag=True):
    """
    :param n: number of jokes2
    :param flag: True
    :return: None
    """
    while n > 0:
        jokes = [choice(nouns)] + [choice(adverbs)] + [choice(adjectives)]
        if flag:
            nouns.remove(jokes[0])
            adverbs.remove(jokes[1])
            adjectives.remove(jokes[2])
        jokes = ' '.join(jokes)
        jokes2.append(jokes)
        n -= 1
    return jokes2
    # print(jokes2)

print(jokes2)
print(get_jokes(5))