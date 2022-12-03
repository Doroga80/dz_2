# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59].

num = int(input('Введите число: '))
lst = []
old = num
if num > 1:
    restart = True
    while restart:
        restart = False
        for i in range(2, num +1):
            if num % i == 0: 
                lst.append(i)
                num = int(num / i)
                restart = True
                break
print(f'{old} -> {lst}')