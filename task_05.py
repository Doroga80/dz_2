# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

from random import randint
n = int(input('Введите размер массива: '))
arrey = []
i = 0
while i < n:
    element = randint(1, 100)
    arrey.append(element)
    i += 1
    
print(arrey)

sort_array = arrey.copy()
size = len(sort_array)
for i in range(size):
    sort_index = randint(0, size - 1)
    temp = sort_array[i]
    sort_array[i] = sort_array[sort_index]
    sort_array[sort_index] = temp
    
print(sort_array)

