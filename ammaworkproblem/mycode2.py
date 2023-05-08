from input import inputFun
from tabulate import tabulate
from pprint import pprint
from operator import itemgetter


w1, w2, w3 = inputFun()


def sortdictitems(d):
    l = {}

    for i, e in enumerate(d):
        sorted_e = sorted([list(item) for item in d[e].items()],
                          key=itemgetter(1), reverse=True)
        l[list(d.keys())[i]] = (sorted_e)

    return l


def parse(w):
    d = {}

    for e in w['incidents']:
        if e['alert'] in d:
            if e['cluster'] in d[e['alert']]:
                d[e['alert']][e['cluster']] += 1
            else:
                d[e['alert']][e['cluster']] = 1
        else:
            d[e['alert']] = {e['cluster']: 1}

    return d


def attach_cluster(wk, srt):
    new = {}
    ld = sortdictitems(parse(wk))

    for k in srt:
        l = []

        if k in ld.keys():
            for v in srt[k]:
                for a in ld[k]:
                    if v[0] == a[0]:
                        v.append(a[1])
                        l.append(v)
                if len(l) == 0 or l[-1][0] != v[0]:
                    v.append(0)
                    l.append(v)
            new[k] = l

        else:
            for v in srt[k]:
                v.append(0)
                l.append(v)
            new[k] = l

    return new


def sortbydict(old, sorted):
    new = {}

    for key in sorted:
        new[key] = old[key]

    return new


def listtodict(lst):
    d = {}
    for e in lst:
        d[e[0]] = e[1:]

    return d


def avgtodict(d):
    new = {}
    for k in d:
        l = []
        for c in d[k]:
            avg = sum([int(char) for char in c[1:]]) / (len(c)-1)
            c.append(avg)
            l.append([c])
        new[k] = l
    return new

ans = attach_cluster(w2, sortdictitems(parse(w1)))

order = {}

for e in ans:
    order[e] = ans[e][0][1]

pprint(avgtodict(sortbydict(ans, listtodict(sorted(order.items(), key=itemgetter(1), reverse=True)))), sort_dicts=False)
