'''
Задача 17
Сложите цифры целого числа.
'''

def sum_diggits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

print(sum_diggits(234234))