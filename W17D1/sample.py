# Example #1 Ternary Operator
# is_good = True
# dragon = "Tootless" if is_good else "Smaug"
# print(dragon)

# Example #2 Random Numbers
# import random
# dragons = ['Puff', 'Toothless', 'Falkor', 'Draco']
# dragonPick = dragons[random.randint(0, len(dragons) - 1)]
# # dragonPick = random.choice(dragons)
# print(dragonPick)

# Example #3 User Input
# answer = input('Who is the coolest dragon? ')
# print(f'You thought {answer} was the coolest dragon...')

# Example #4 Importing Files
f = open("words.txt", "r")
print(f)
words = [ x.split(',') for x in f ][0]
print(words)