# Task 20

def Taylors_row(x):
    expressions = []
    counter = 1
    precision = 8

    while True: 
        expression = (-1)**(counter-1) * x**counter/ counter
        counter += 1
        if abs(expression) < 10**-6:
            break
        expressions.append(expression)

    answ = sum(expressions)

    return round(answ, 8)

x = float(input())
result = Taylors_row(x)
print(result)