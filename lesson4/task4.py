# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.


import task2

print(task2.currency_rates('55'))
print(task2.currency_rates('prob'))
print(task2.currency_rates('ProBB'))
print(task2.currency_rates('a'))
print(task2.currency_rates())