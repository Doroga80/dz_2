# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоретет операций стандартный.
# Добавте возьожность использования скобок, меняющтй приоретет операций.
# Пример:
# 1+1*3 => 7;
# (1+2)*3 => 9;

str = '(3+2)*2'
print(eval(str))