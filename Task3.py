'''
Задача 3
Отсортируйте словарь по значению в порядке возрастания и убывания.
'''

import operator
a = {'a': 1, 'b': 2, 'c': 3, 'd': 0}
res1 = dict(sorted(a.items(), key=operator.itemgetter(1)))
res2 = dict(sorted(a.items(), key=operator.itemgetter(1), reverse=True))
print(res1)
print(res2)