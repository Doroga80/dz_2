# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]


my_lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
new_lst = []
for i in my_lst:
    if  my_lst.count(i) == 1:
            new_lst.append(i)
            
print(f'Исходный список: {my_lst} -> {new_lst}')