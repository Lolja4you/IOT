import json

import pandas as pd
from io import StringIO


def main(enviromen, request):
    return 'Hello'

def yndx(enviromen, request):
    return  parser('YNDX_230416_240417.txt')

def gazp(enviromen, request):
    return  parser('GAZP_230416_240417.txt')

def chmf(enviromen, request):
    return parser('CHMF_230416_240417.txt')


def parser(file_path, base_dir=None):
    # Преобразование строки в список стро
    # column_names = ['TICKER', 'PER', 'DATE', 'TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL']
    df = pd.read_csv(file_path, skiprows=1, header=None, names=['TICKER', 'PER', 'DATE', 'TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL'])

    # Преобразуем столбец DATE и TIME в datetime
    # df['DATE'] = pd.to_datetime(df['DATE'].astype(str) + df['TIME'].astype(str), format='%y%m%d%H%M%S')

    # Устанавливаем DATE в качестве индекса
    # df.set_index('DATE', inplace=True)

    # Удаляем столбец TIME, так как он больше не нужен
    # df.drop('TIME', axis=1, inplace=True)

    # Выводим DataFrame
    # print(df)
    data_dict = {
        'HEADER': df.columns.to_list(),
        'DATA': df.to_dict(orient='records')
    }

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_dict)

    return json_data
    