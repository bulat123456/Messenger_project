import yaml

data = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_ptice': {'computer': '200€-1000€',
                           'printer': '100€-300€',
                           'keyboard': '5€-50€',
                           'mouse': '4€-7€'}
        }

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False
              )

with open("file.yaml", 'r', encoding='utf-8') as f:
    data_out = yaml.load(f, Loader=yaml.SafeLoader)

print(data == data_out)