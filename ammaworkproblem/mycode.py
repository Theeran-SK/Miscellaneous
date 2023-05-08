from input import inputFun
import operator
from pprint import pprint
from tabulate import tabulate

w1, week2, w3 = inputFun()

dict1 = {}
dict2 = {}

for each_ele in w1['incidents']:
    if each_ele['alert'] in dict1:
        dict1[each_ele['alert']] += 1
    else:
        dict1[each_ele['alert']] = 1

sorted_week1_dict = sorted([list(item) for item in dict1.items()], key=operator.itemgetter(1), reverse=True)
print(sorted_week1_dict)

def dict_alerts(week2, sorted_week1_dict, dict2):
    for e in week2['incidents']:
        if e['alert'] in dict2:
            dict2[e['alert']] += 1
        else:
            dict2[e['alert']] = 1

    for i, e in enumerate(sorted_week1_dict):
        if sorted_week1_dict[i][0] in dict2.keys():
            sorted_week1_dict[i].append(dict2[sorted_week1_dict[i][0]])
        else:
            sorted_week1_dict[i].append(0)
    
    return sorted_week1_dict

# for e in w2['incidents']:
#     if e['alert'] in dict2:
#         dict2[e['alert']] += 1
#     else:
#         dict2[e['alert']] = 1

# for i, e in enumerate(d1):
#     if d1[i][0] in dict2.keys():
#         d1[i].append(dict2[d1[i][0]])
#     else:  
#         d1[i].append(0)

table = dict_alerts(week2, sorted_week1_dict, dict2)

print(tabulate(table, headers=('alert', 'w1', 'w2')))

