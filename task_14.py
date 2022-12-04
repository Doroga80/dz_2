# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

# запись в файл
def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)
        
 # создаём случайное число       
def rnd():
    return random.randint(0, 101)

# создание коэффициентов многочлена
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst

# создание многочлена в виде строки
def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                    wr += f'{lst[i]}x^{len(lst) - i - 1}'
                    if lst[i + 1] != 0:
                        wr +='+'
                    elif i == len(lst) - 2 and lst[i] != 0:
                        wr += f'{lst[i]}x'
                        if lst[i + 1] != 0:
                            wr +='+'
                    elif i == len(lst) - 1 and lst[i] != 0:
                        wr += f'{lst[i]} = 0'
                    elif i == len(lst) - 1 and lst[i] == 0:
                        wr +='= 0'
    return wr


# создание файла    
k1 = int(input('Введите натуральную степень k -'))
koef1 = create_mn(k1)
write_file('file33_1.txt', create_str(koef1))
