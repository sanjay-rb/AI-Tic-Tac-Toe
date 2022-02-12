from itertools import permutations

import csv
'''
x,
x,
x,
o,
o
b,
b,
b,
b,
'''
sl = ['xxx', 'oob', 'bbb']
s = ''.join(sl)

def getIntex(l, v):
    indices = []
    for i in enumerate(l):
        if i[1] == v:
            indices.append(str(i[0]))
    return indices

val = sorted(list(set(permutations(s))))
des_list = []
for v in val:
    v = list(v)
    v.append(f"x={','.join(getIntex(v, 'x'))}; o={','.join(getIntex(v, 'o'))}")
    des_list.append(v)
print(des_list)
final_list = []
for d in des_list:
    xi = getIntex(d, 'x')
    oi = getIntex(d, 'o')
    cp = d.copy()
    for i in range(0, 8+1):
        if str(i) in xi+oi:
            continue
        else:
            final_list.append(cp+[i])
print(final_list)

filename = "test.csv"
    
with open(filename, 'w', newline='', encoding='utf-8') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow([0, 1, 2, 3, 4, 5, 6, 7, 8, 'd', 'o'])
    csvwriter.writerows(final_list) 