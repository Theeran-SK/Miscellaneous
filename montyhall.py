from random import shuffle

doors = ['goat', 'goat', 'car']

fail = 0
success = 0

for x in range(100000):
    shuffle(doors)

    d1 = doors[0]
    d2 = doors[1]
    d3 = doors[2]

    if d1 == 'goat':
        if d3 == 'car':
            success += 1
        else:
            fail += 1

    else:
        if d1 == 'car':
            success += 1
        else:
            fail += 1
    

print(str(round(100*(success/100000), 2)) + '%')
