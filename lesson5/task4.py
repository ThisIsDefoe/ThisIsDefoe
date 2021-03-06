# Представлен список чисел.
# Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
#
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []

for i in range(1, len(src)):
    if src[i] > src[i -1]:
        result.append(src[i])
print(result)

start = perf_counter()
print(result)
finish = perf_counter()
print('Speed: ', finish - start)