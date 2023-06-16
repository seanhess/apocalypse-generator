cmd = input()
import random

def roll(cmd):
    total = 0
    dice = []
    count, sides = cmd.split("d")
    count, sides = int(count), int(sides)
    for num in range(count):
        die = random.randint(1, sides)
        dice.append("die #"+str(num+1)+': ' + str(die))
        total = total + die
    return total, dice

total, dice = roll(cmd)
print(total)
for die in dice:
    print(die)