# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться

import random

# запись в файл
def write_file(name, st):
    with open(name, 'w') as date:
        date.write(st)
        
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

# получения степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получкние коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получения его коэффициентов
def colc_mn(st):
    st = st[0].replace(' ','').split('=')
    st = st[0].split('+')
    lst =[]
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = i -1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(str[ii]) == i:
            lst.append(k_mn(str[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
            
    return lst



# создание двух файлов
k1 = int(input('Введите натуральпую степень для файла №1: '))
k2 = int(input('Введите натуральпую степень для файла №2: '))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file('file33_1.txt', create_str(koef1))
write_file('file33_2.txt', create_str(koef2))


# нахождение суммы многочленов
with open('file33_1.txt', 'r') as date:
    st1 = date.readlines()
with open('file33_2.txt' 'r') as date:
    st2 = date.readlines()
print(f'Первый многочлен {st1}')
print(f'Второй многочлен {st2}')
lst1 = create_mn(st1)
lst2 = create_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new + [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file('file34_res.txt', create_str(lst_new))
with open('file34_res txt', 'r') as date:
    st3 = date.readlines()
print(f'Результат многочлена{st3}')