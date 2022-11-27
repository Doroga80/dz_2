# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11

# num = int(input('Введите число: '))
# sum = 0
# while(num !=0):
#     sum = sum + num % 10
#     num = num // 10
# print('Сумма цифр равна:', sum)

def sum_in_number(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

n = list(input('Введите число: '))
print(sum_in_number(n))