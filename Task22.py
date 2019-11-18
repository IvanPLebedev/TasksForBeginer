'''
Задача 22
Напишите программу, которая принимает текст и выводит два слова: наиболее часто
встречающееся и самое длинное.
'''
import collections

text = 'Напишите программу и которая принимает текст и выводит два слова наиболее часто встречающееся и самое длинное'
words = text.split()
counter = collections.Counter(words)
common, occurrences = counter.most_common()[0]
longest = max(words, key=len)
print(occurrences)
print(common, longest)