# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
# например, во фреймворке django.


import os
import shutil
from pathlib import *

my_authapp = Path.cwd() / 'my_project' / 'authapp'
my_mainapp = Path.cwd() / 'my_project' / 'mainapp'
templates_dir = Path.cwd() / 'my_project' / 'templates'
templates_authapp = Path.cwd() / 'my_project' / 'templates' / 'authapp'
templates_mainapp = Path.cwd() / 'my_project' / 'templates' / 'mainapp'

templates_dir.mkdir(exist_ok=True)
templates_authapp.mkdir(exist_ok=True)
templates_mainapp.mkdir(exist_ok=True)

for file in os.listdir(my_authapp):
    try:
        if file == 'base.txt' or file == 'index.txt':    # или file.endswith('.html') если шла бы речь только о html
            shutil.copy(os.path.join(my_authapp, file), os.path.join(templates_authapp, file))
    except PermissionError:
        print(f'Файлы успешно скопированы!')
for file in os.listdir(my_mainapp):
    try:
        if file == 'base.txt' or file == 'index.txt':
            shutil.copy(os.path.join(my_mainapp, file), os.path.join(templates_mainapp, file))
    except PermissionError:
        print(f'Файлы успешно скопированы!')