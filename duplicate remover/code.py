with open("duplicate remover/input") as file:
    inputdata = file.read().strip().split("\n")

not_dupe = [i for i in inputdata if inputdata.count(i) == 1]


print(not_dupe)