'''
Напишите программу, которая принимает два списка и выводит все элементы первого,
которых нет во втором.
'''

a = list('s;dfkl;saflkdfk;dls')
b = list('dmfklwokdm')

res = list(set(a) - set(b))
print(res)