import random
import math

students = [ 'Alex Clough', 'Bianca Salinas', 'David Kim', 'Earl Woo', 
'Ellen Park', 'Hector Crespo', 'Jack Radinger', 'James Sullivan', 'Jessica Thornton',
'Jonathan Chan', 'Kevin Zheng', 'Kyle Powers', 'Lisa Hoque', 'Miguel Flores',
'Nurs Asanov', 'Schuler Small', 'Zane Preudhomme' ]

random.shuffle(students)
middle = math.ceil(len(students)/2)
first = students[0:middle]
second = students[middle:]

print('Standup 1')
print('-' * 10)
for student in first:
    print(student)
print(' ')
print('Standup 2')
print('-' * 10)
for student in second:
    print(student)