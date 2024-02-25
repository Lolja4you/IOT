# Task 16

def check_point(x0, y0):
    circle_condition = (x0-1)**2 + y0**2 <= 2**2 and (x0-1)**2 + y0**2 >= 1**2
    rectangle_condition = abs(x0 - 4) < 2 and abs(y0 - 2) < 3

    if circle_condition and rectangle_condition:
        return 'yes yes'
    elif circle_condition:
        return 'yes no'
    elif rectangle_condition:
        return 'no yes'
    else:
        return 'no no'

x0, y0 = map(float, input().split())
print(check_point(x0, y0))
