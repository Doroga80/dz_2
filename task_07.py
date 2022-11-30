# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]

number =  [2, 3, 5, 6]
new_number = []
last = len(number) - 1
for i in range(0, (last // 2) + 1):
    temp = number[i] * number[last]
    new_number.append(temp)
    last -= 1

print(f'{number} => {new_number}')
    
    
    


        
    
print(f'Произведение пар чисел списка {list}')