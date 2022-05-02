"""Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык"""

def num_translate():
    number = input()
    print(number.get(number.lower()))

numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

num_translate()