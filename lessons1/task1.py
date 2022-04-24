# ### 1. Реализовать вывод информации о промежутке времени
# в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

# time = int(input("Введите время в секундах "))
# days = time // 86400
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# if time < 60:
#     print(f"секунд {seconds}")
# elif minutes > hours:
#     print(f"минут: {minutes} секунд: {seconds}" )
# elif hours > :
#     print(f"часов: {hours} минут: {minutes} секунд: {seconds}")
# else:
#     print(f"дней: {days} часов: {hours} минут: {minutes} секунд: {seconds}" )

# duration = int(input("Введите секунды: "))
# minutes = duration // 60
# hour = minutes // 60
# day = hour // 24
#
# if duration < 60:
#     print(duration, "сек")
# if 60 <= duration < 3600:
#     if duration % 60 == 0:
#         print(minutes, "мин")
#     else:
#         print(minutes, "мин", duration % 60, "сек")
# elif 3600 <= duration < 86400:
#     if minutes % 60 == 0:
#         if duration % 60 == 0:
#             print(hour, "час")
#         else:
#             print(hour, "час", duration % 60, "сек")
#     if minutes % 60 != 0:
#         if duration % 60 == 0:
#             print(hour, "час", minutes % 60, "мин")
#         else:
#             print(hour, "час", minutes, "мин", duration % 60, "сек")
# elif duration >= 86400:
#     if hour % 24 == 0 and minutes % 60 == 0 and duration % 60 == 0:
#         print(day, "дн")
#     elif hour % 24 == 00 and minutes % 60 == 0:
#         print(day, "дн", duration % 60, "сек")
#     elif hour % 24 == 0 and duration % 60 == 0:
#         print(day, "дн", minutes % 60, "мин")
#     elif hour % 24 == 0:
#         print(day, "дн", minutes, "мин", duration % 60, "сек")
#     else:
#         print(day, "дн", hour % 24, "час", minutes % 60, " мин", duration % 60, "сек")




# #2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

# cube_list = []
# for numbers in range(1, 1000+1, 2):
#     cube = numbers ** 3
#     cube_list.append(cube)
# print(cube_list)
# # Получил список с нечетными кубическими числами
#
# cube_list2 = []
# for el in cube_list:
#     summ = 0
#     while el > 0:
#         m = el % 10
#         summ = summ + m
#         el = el // 10
#     cube_list2.append(summ)
# # Получилась сумма нечетных чисел
#
# summ_list = 0
# for i in range(len(cube_list2)):
#     if cube_list2[1] % 7 == 0:
#         summ_list = summ_list + cube_list[1]
# print(summ_list)
#
# cube_list3 = []
# for i in cube_list2:
#     i += 17
#     cube_list3.append(i)
# #print(cube_list3) Проверка списка на прибавление 17
#
# summ_list2 = 0
# for i in range(len(cube_list3)):
#     if cube_list3[i] % 7 == 0:
#         summ_list2 = summ_list2 + cube_list[i]
# print(summ_list2)


#3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел
# в интервале от 1 до 100:

numbers = []
for i in range(100):
    i = i + 1
    if i in numbers:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif i % 10 > 1 and i % 10 <5:
        print(i, "процента")
    else:
        print(i, "процентов")

