# Задайте список из n чисел последовательности (1 + 1 / n)**n
# и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.49, 2.52]     ->       14.07
# (Округлять не обязательно)

def list_with_posledovatelnosti(n):
    summ =[((1 + 1 / i)**i) for i in range(1, n + 1)]
    return sum(summ)

print(list_with_posledovatelnosti(4))
