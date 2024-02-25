# Task23
def my_filter(a):
    print(*map(lambda x: int(x)*10, a))
# my_filter(input().split())


# Task24
# Интеграл
import math
def trapez(func, a, b, N):
    h = (b - a) / N 
    result = 0.5 * (func(a) + func(b)) 
    for i in range(1, N):
        result += func(a + i * h)
    return round(result * h, 8)

def determinated_func(func)->any:
    """Returns:\n
     - Возвращает lambda функцию приведенное к эквивалентному в языке python  
    """
    return eval(func)

# func_name, a, b, N = input().split()
# print(trapez(determinated_func(func_name), float(a), float(b), int(N)))


# Task 25
# answ: 4 
def function(a = 1, b = 2, c = 3):
 return int(a + b / c)
# print(function(2, c = 1, b = 2))


# Task 26 
# [4,6]
def func(*args):
    lst = []
    for item in args:
        if item & 1 == 0: lst.append(item) 
    return lst
# a, *b, c = func(1, 2, 3, 4, 5, 6, 7, 8)
# print(b)


# Task 27 
def volume(*args):
    from functools import reduce
    if len(args) > 3: return f'Error: len args must be 2 or 3 but given {len(args)}'
    return reduce(lambda x, y: x * y, args)
# print(volume(*map(int, input().split())))


# Task 28
# answ: 8
y = lambda a, b: a ** b;print(y(2, 3))
