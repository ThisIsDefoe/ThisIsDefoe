# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация:
# выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только
# методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли
# усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

import requests


def currency_rates(param):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encoding = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encoding)  # str
    if param.upper() not in content:
        return None
    elif param.islower() or param.isdigit():
        return None
    else:
        content = content.split('</Valute>')
        for el in content:
            el = ''.join(el)
            if param.upper() in el:
                a = el[el.find('<Value>') + 7: el.find('</Value>')]
                b = el[el.find('<Nominal>') + 9: el.find('</Nominal>')]
                return f'{b} {param} = {a} рублей'


# print(currency_rates(input('Введите код валюты: '))) #с импутом
print(currency_rates('USD'))  # без инпута
print(currency_rates('EUR'))