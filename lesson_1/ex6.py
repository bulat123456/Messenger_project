with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write('сетевое программирование\n')
    f.write('сокет\n')
    f.write('декоратор\n')

with open('test_file.txt', encoding='utf-8') as t_f:
    for each_line in t_f:
        print(each_line, end="")