# Example #1 Ternary Operator
# is_good = True
# dragon = "Tootless" if is_good else "Smaug"
# print(dragon)

#example #2 Random Numbers
import random
dragons = ['Puff', 'Toothless', 'Falkor', 'Draco']
dragonPick = dragons[random.randint(0, len(dragons) - 1)]
# dragonPick = random.choice(dragons)
print(dragonPick)