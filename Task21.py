'''
Задача 21
Нужно проверить, все ли числа в последовательности уникальны.
'''

a = [12, 2, 3, 4, 6, 7, 8, 9]
b = [12, 2, 3, 4, 6, 7, 8, 9, 2]

def unique(li):
    return len(li) == len(set(li))

print(unique(a))
print(unique(b))