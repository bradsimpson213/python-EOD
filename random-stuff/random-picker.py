import random
import math

students = [ 'David Kim', 'James Sullivan' ]


student = random.choice(students)
print('Next person to present is...')
print(student)

# random.shuffle(students)
# middle = math.ceil(len(students)/2)
# first = students[0:middle]
# second = students[middle:]

# 
# print('-' * 10)
# for student in first:
#     print(student)
# print(' ')
# print('Standup 2')
# print('-' * 10)
# for student in second:
#     print(student)