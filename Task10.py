'''
Задача 10
Вы принимаете от пользователя последовательность чисел, разделённых запятой.
Составьте список и кортеж с этими числами.
'''
a = '1,2,12,3,4,5,6,4,55,3,3'

b = a.split(',')
li = list(map(int, b))
tu = tuple(li)
print(li)
print(tu)