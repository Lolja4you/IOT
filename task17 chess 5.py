# Task 17
# принцип лежит в том что является ли сейчас ячейка четной при сумме данного row и прибавленного к нему col
# a1;2ч
# a1 квадрант на доске;2ч его значение
# 2 - сумма
# ч = черный; бел =б
# +---------+--------+---------+---------+---------+---------+---------+---------+---------+
# | col\Row |   a    |    b    |    c    |    d    |    e    |    f    |    g    |    h    |
# +---------+--------+---------+---------+---------+---------+---------+---------+---------+
# |    8    | a8(9б) | b8(10ч) | c8(11б) | d8(12ч) | e8(13б) | f8(14ч) | g8(15б) | h8(16ч) |
# |    7    | a7(8ч) |  b7(9б) | c7(10ч) | d7(11б) | e7(12ч) | f7(13б) | g7(14ч) | h7(15б) |
# |    6    | a6(7б) |  b6(8ч) |  c6(9б) | d6(10ч) | e6(11б) | f6(12ч) | g6(13б) | h6(14ч) |
# |    5    | a5(6ч) |  b5(7б) |  c5(8ч) |  d5(9б) | e5(10ч) | f5(11б) | g5(12ч) | h5(13б) |
# |    4    | a4(5б) |  b4(6ч) |  c4(7б) |  d4(8ч) |  e4(9б) | f4(10ч) | g4(11б) | h4(12ч) |
# |    3    | a3(4ч) |  b3(5б) |  c3(6ч) |  d3(7б) |  e3(8ч) |  f3(9б) | g3(10ч) | h3(11б) |
# |    2    | a2(3б) |  b2(4ч) |  c2(5б) |  d2(6ч) |  e2(7б) |  f2(8ч) |  g2(9б) | h2(10ч) |
# |    1    | a1(2ч) |  b1(3б) |  c1(4ч) |  d1(5б) |  e1(6ч) |  f1(7б) |  g1(8ч) |  h1(9б) |
# +---------+--------+---------+---------+---------+---------+---------+---------+---------+


def check_color(cell):
    letters = 'abcdefgh'
    row, col = cell[0], int(cell[1])

    if (letters.index(row)+1 + col)&1 == 0:
        return 'black'
    return 'white'
    #     return 'ч'
    # return 'б'

# cell = input()
# print(check_color(cell))

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['col\Row', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def out_space():
    letters = 'abcdefgh'
    
    space = []

    for column in range(0,8):
        space.append([1,2,3,4,5,6,7,8])
        for letter in letters:
            let_ind = letters.index(letter)
            cell = letter+str(column+1)
            space[column][let_ind] = f'{letter}{column+1}({let_ind+column+2}{check_color(cell)})'
    
    for i, row in enumerate(space[::-1], 1):
        table.add_row([f'{9-i}', *row])

    print(table)

# out_space()