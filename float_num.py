#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
#координат точек в этой четверти (x и y).

number1 = int(input('Введите номир четверти оси: '))

if number1 == 1:
    print('Первая ось: x > y and x > y')
elif number1 == 2:
    print('Вторая ось: x < 0 and y > 0')
elif number1 == 3:
    print('Третья ось x < 0 and y > 0')
elif number1 == 4:
    print('Четвертая ось x > 0 and y < 0')