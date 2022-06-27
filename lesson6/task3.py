# * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Также реализовать парсинг данных из файлов - получить отдельно
# фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в
# какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор
# типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться
# данные, полученные в результате парсинга.
#
# ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать путь к обоим исходным файлам и путь к выходному файлу со словарём. Проверить
# работу скрипта для случая, когда все файлы находятся в разных папках.

import json
from sys import argv
import os

PATH_DICT = {
    'FILE_USERS_PATH': os.path.join(os.path.curdir, 'users.csv'),
    'FILE_HOBBY_PATH': os.path.join(os.path.curdir, 'hobby.csv'),
    'FILE_RESULT_PATH': os.path.join(os.path.curdir, 'users_hobby.json')
}

PATH_DICT.update(zip(('FILE_USERS_PATH', 'FILE_HOBBY_PATH', 'FILE_RESULT_PATH'), argv[1:]))

TPL = ('last_name', 'first_name', 'middle_name', 'hobby_name')

with open(PATH_DICT['FILE_USERS_PATH'], encoding='utf-8') as user_src:
    with open(PATH_DICT['FILE_HOBBY_PATH'], encoding='utf-8') as hobby_src:
        with open(PATH_DICT['FILE_RESULT_PATH'], 'w', encoding='utf-8') as output:
            output.write('{"data": [\n')
            record = None
            while True:
                try:
                    user = next(user_src)
                except StopIteration:
                    break
                user = user.rstrip('\n').split(',')

                try:
                    hobby = next(hobby_src)
                except StopIteration:
                    hobby = None
                else:
                    hobby = hobby.rstrip('\n')

                if record:
                    output.write(',\n')

                record = dict(zip(TPL, (*user, hobby)))
                output.write(json.dumps(record, ensure_ascii=False))

            output.write('\n]}\n')

        try:
            hobby = next(hobby_src)
        except StopIteration:
            pass
        else:
            os.remove(PATH_DICT['FILE_RESULT_PATH'])
            raise ValueError('Invalid data source')