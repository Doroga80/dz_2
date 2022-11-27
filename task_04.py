# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции вводятся с клавиатуры.

n = int(input('Введите число: '))
array = list(range(-n, n + 1))
size = len(array)
avg = 1
print(array)
print('Для окончание ввода нажмите пробел')
while True:
    index = input(f'Введите индекс для нахождения\
        произведения( от 0 до {size-1})')
    if index == '':
        break
    else:
        for i in array:
            if i == array[int(index)]:
                avg = avg * i
print(avg)