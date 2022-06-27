# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?


import os


def my_project(name):
    try:
        my_project_dir = os.path.join('my_project', name)
        os.makedirs(my_project_dir, exist_ok=True)
    except:
        print('Введите название папки в ковычках!')


print(my_project('Test_1'))

# Второе решение:
# my_settings = os.path.join('my_project', 'settings')
# my_mainapp = os.path.join('my_project', 'mainapp')
# my_admiapp = os.path.join('my_project', 'admiapp')
# my_authapp = os.path.join('my_project', 'authapp')
#
# os.makedirs(my_settings, exist_ok=True)
# os.makedirs(my_mainapp, exist_ok=True)
# os.makedirs(my_admiapp, exist_ok=True)
# os.makedirs(my_authapp, exist_ok=True)