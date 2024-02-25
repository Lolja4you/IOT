def data_max(mass:list)->int:
    """
     Returns the index from the list -> int\n
     Return raise on failure
    """
    if not isinstance(mass, list):
        raise TypeError(f'mass must be list, but given mass_type: {type(mass)} ::: mass_value: {mass}  ')
    return mass.index(max(mass[:11]))

#answ: 0
# print(data_max([7.713, 0.208, 6.336, 7.488, 4.985, 2.248, 1.981, 7.605, 1.691, 0.883, 6.854, 9.534, 0.039, 5.122, 
# 8.126, 6.125, 7.218, 2.919, 9.178, 7.146, 5.425, 1.422, 3.733, 6.741, 4.418]))


#answ: Traceback (most recent call last):
#   File "D:\Main_tmp_data\Documents\code\python\IOT\task8.py", line 23, in <module>
#     print(data_max('ss'))
#           ^^^^^^^^^^^^^^
#   File "D:\Main_tmp_data\Documents\code\python\IOT\task8.py", line 7, in data_max
#     raise TypeError(f'mass must be list but given mass_type: {type(mass)} ::: mass_value: {mass}  ')
# TypeError: mass must be list but given mass_type: <class 'str'> ::: mass_value: ss
# print(data_max('ss'))