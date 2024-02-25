room = int(input("Введите номер квартиры: "))
if 1 <= room <= 32:
    #если мы достигли предела этажей в подъезде, то у нас к целой части от деления прибавляется единица. 
    #room-1 нужно чтобы мы могли посчитать 8 этаж. 
    entrance = (room - 1) // 8 + 1 

    #поулчая остаток от деления мы находим на каком этаже расположена квартира 
    #остататок от деления работает по принципу какое наименьше и ближайшее число делиться на 8, для 31 это будет 24 (31-24)=7 -->
    #--> что соотвествует номеру этажа ниже
    #room-1 нужно чтобы мы могли посчитать 8 этаж. 
    floor = (room - 1) % 8 + 1
    print(f"{floor} {entrance}")
else:
    print("Номер квартиры должен быть от 1 до 32.")