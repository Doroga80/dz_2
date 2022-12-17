# человек против бота с интеллектом

from random import randint

def input_dat(name):
    x = int(input(f'{name}, Введите колличество конфет, от 1 до 28: ' ))
    while x < 1 or x >28:
        x = int(input(f'{name}, Введите корректное колличество конфет:  '))
    return x


def p_print(name, k, counter, value):
    print(f'Ходит {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.')
    
    
def bot_calc(value):
    k = randint(1, 28)
    while value-k <= 28 and value > 29:
        k = randint(1, 29)
    return k
    
    
player1 = input('Введите имя первого игрока: ')
player2 = 'Bot'
value = int(input('Введите колличество конфет: '))
flag = randint(0,2)
if flag:
    print('Первый ход {player1}')
else:
    print('Первый ход {player2}')
    
counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k , counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)
        
if flag:
    print(f'Поздравляем! Победил {player1}')
else:
    print(f'Пщздравляем! Победил {player2}')