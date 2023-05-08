from itertools import count
from random import choice

chance = ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 't']
works = 0

for i in range(100000):
    outcomes = []
    for x in range(10):
        outcomes.append(choice(chance))
    if outcomes.count('h') >= 3:
        works += 1

print(works)