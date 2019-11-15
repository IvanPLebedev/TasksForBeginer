'''
Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово
или фраза, которые одинаково читаются слева направо и справа налево
'''

def polindrom(string):
    if string == string[::-1]:
        return True
    else:
        return False


a = 'asdfdsa'
b = 'reewer'

for x in [a,b]:
    if polindrom(x):
        print(x,': polindrom')
    else:
        print(x,': don,t polindrom')
