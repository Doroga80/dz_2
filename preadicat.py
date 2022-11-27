#Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Примечание:
#Используйте знания об Алгебра Логике, вы должны перебрать все возможные
# комбинации значений X, Y, Z (принимают значения 0 или 1)

X = int(input('Введите число X: '))
Y = int(input('Введите число Y: '))
Z = int(input('Введите число Z: '))

a = X * Y * Z
b = X + Y + Z

if a > 0:
    a = 0
elif a < 1:
    a = 1
if b > 0:
    b = 0
elif b < 1:
    b = 1

if a == b:
    print('Истинна')
elif a != b:
    print('Ложно')

leftSide = not (X or Y or Z)
rightSide = not (X and Y and Z)
result = leftSide == rightSide

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
