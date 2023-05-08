with open("pwdecoding/possibilities.txt") as file:
    data = file.read().strip().split('\n')
    
def check(l, s):
    common = [e for e in l if e in s]
    return len(common)

for i in data:
    if len(i) != 6:
        data.remove(i)

for i in data:
    if len(i) == 1 or len(i) == 0:
        data.remove(i)

two = ['a', 'b', 'c']
three = ['d', 'e', 'f']
four = ['g', 'h', 'i']
five = ['j', 'k', 'l']
six = ['m', 'n', 'o']
nine = ['w', 'x', 'y', 'z']

keypad = [two, three, four, five, six, nine]

final = []

for i in data:
    flag = True
    for j in keypad:
        if check(j, i) != 1:
            flag = False
    if flag == True:
        final.append(i)

print(final)