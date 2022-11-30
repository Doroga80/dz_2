# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

numbers = int(input('Введите число: '))
fib = []
fib_1 = 1
fib_2 = -1
i =0
while i < numbers:
    fib.insert(0, fib_1)
    temp = fib_1
    fib_1 = fib_2
    fib_2 = temp-fib_2
    i += 1
    
fib_1 = 0
fib_2 = 1
i = 0
while i <= numbers:
    fib.append(fib_1)
    temp = fib_1
    fib_1 = fib_2
    fib_2 += temp
    i += 1
    
print(fib)