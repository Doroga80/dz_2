# Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import*


getcontext().prec = 3

def nilakantha(reps):
    result = Decimal(0.01)
    op = 1
    n = 2
    for n in range(2 *reps + 1):
        result += 4/Decimal(n*(n + 1) + (n + 2)* op)
        op *= -1
    return result


print('Сколько повторений?')
repetitions = int(input())
print(nilakantha(repetitions))
print('3.141')      

