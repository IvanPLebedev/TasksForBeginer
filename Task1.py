'''
Задача 1
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
Выведите все элементы, которые меньше 5.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def elements_less_then(x, ar):
    res = list(filter(lambda y: y < x, ar))
    return res

print(elements_less_then(5, a))