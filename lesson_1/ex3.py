a = 'attribute'
b = 'класс'
c = 'функция'
d = 'type'

list = [a, b, c, d]
for i in list:
    try:
        print(eval(f'b"{i}"'))
    except Exception:
        print(f'Слово "{i}" нельзя перевести в байты')