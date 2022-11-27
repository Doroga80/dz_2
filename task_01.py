# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11

def sum_in_number(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

n = list(input('Введите число: '))
print(sum_in_number(n))
