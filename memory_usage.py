from pympler import asizeof
from prettytable import PrettyTable

table = PrettyTable(['№','Datatypes and datastructures', 'size in memory'])

array = [
    ['1', 'Пустой список', str(asizeof.asizeof(list()))],
    ['2', 'Пустой словарь', str(asizeof.asizeof(dict()))],
    ['3', 'Пустое множество', str(asizeof.asizeof(set()))],
    ['4', 'Пустая строка', str(asizeof.asizeof(' '))],
    ['5', 'Пустой кортеж', str(asizeof.asizeof(tuple()))],
    ['6', 'Integer', str(asizeof.asizeof(1))],
    ['7', 'Char', str(asizeof.asizeof('a'))],
    ['8', 'Float', str(asizeof.asizeof(1.0))],
    ['9', 'None', str(asizeof.asizeof(None))],
    ['10', 'True', str(asizeof.asizeof(True))],
    ['11', 'False', str(asizeof.asizeof(False))],
]

for row in array:
    table.add_row(row)

print(table)
