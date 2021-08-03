str_a = b'class'
str_b = b'function'
str_c = b'method'

list = [str_a, str_b, str_c]

for i in list:
    print(f'тип: {type(i)}')
    print(f'содержимое: {i}')
    print(f'длинна: {len(i)}')