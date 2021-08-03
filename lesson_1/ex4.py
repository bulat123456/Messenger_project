VAR_1_STR = 'разработка'
VAR_2_STR = 'администрирование'
VAR_3_STR = 'protocol'
VAR_4_STR = 'standard'

STR_LIST = [VAR_1_STR, VAR_2_STR, VAR_3_STR, VAR_4_STR]

list = []
for i in STR_LIST:
    el_b = i.encode('utf-8')
    list.append(el_b)

print(f'{list}\n')

list_str = []
for i in list:
    el_str = i.decode('utf-8')
    list_str.append(el_str)

print(list_str)
