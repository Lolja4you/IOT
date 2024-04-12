# Task 29

# В каких директориях python ищет модули по умолчанию?
# o Корневая директория
# o Домашняя директория программы
# o На рабочем столе
# answ: ->
# -> Корневая директория
# -> Домашняя директория программы


# Task 30 

# Модулем на языке Python является
# o Любой текстовый файл с инструкциями на языке Python с расширением .py
# o Любой текстовый файл с инструкциями на языке Python
# o Любой текстовый файл с инструкциями на языке Python с расширением .pyc
# 
# answ: -> o Любой текстовый файл с инструкциями на языке Python с расширением .py


# Task 31
def write_a(filename, data):
    import os, datetime
    directory = 'data_dir'
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, filename), 'a+') as data_a:
        data_a.write('-'*31+'\n')
        data_a.write('Series'+'\n')
        data_a.write(datetime.datetime.now().strftime('Time: %H:%M:%S Date: %d.%m.%Y') + '\n')
        data_a.write('-'*31+'\n')
        data_a.write('time value'+'\n')
        for item in data:
            data_a.write('\t'.join(map(str, item)) + '\n')

# write_a("1.txt", [(1, 20),(2, 30),(3, 40),(4, 35),(5, 22),(6, 10)])
    

# Task 32
def generate_file(rows, columns, filename = 'freqs.txt'):
    import random, os, datetime
    directory = 'data_dir'
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, filename), 'a+') as data_a:
        for _ in range(rows):
            row_values = [f"{random.uniform(10, 12):.4f}" for _ in range(columns)]
            data_a.write(";".join(row_values) + '\n')

# generate_file(1000, 4)
            
def frequency_filter(a, filename='freqs.txt'):
    import random, os, datetime
    directory = 'data_dir'
    if not os.path.exists(os.path.join(directory, filename)):
        raise FileExistsError(f'{os.path.join(directory, filename)} not found')

    data = []
    with open(os.path.join(directory, filename), 'r') as file:
        for _ in range(100):
            line = file.readline().strip()
            data.extend(map(float, line.split(';')))
    filtered_data = [value for value in data if value <= a]
    filtered_data.sort()
    return filtered_data

print(*frequency_filter(float(input())))
