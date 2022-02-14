from itertools import permutations
import csv
from pickle import FALSE

from numpy import False_
ts = [
    'xbbbbbbbb',
    'xoxbbbbbb',
    'xoxoxbbbb',
    'xoxoxoxbb',
    'xoxoxoxox',
]

# %%
for i in sorted(list(set(permutations(ts[0])))):
    print(i)

# %%
x_wins = [
    "0,1,2",
    "3,4,5",
    "6,7,8",
    "0,3,6",
    "1,4,7",
    "2,5,8",
    "0,4,8",
    "2,4,6",
]

def getIntex(l, v):
    indices = []
    for i in enumerate(l):
        if i[1] == v:
            indices.append(str(i[0]))
    return indices

def isXWins(xi):
    for win in x_wins:
        if win in xi or win == xi:
            return True
    return False

def getOiList(x_xombination):
    xi = getIntex(x_xombination, 'x')
    xis = ','.join(xi)
    ois = []
    x_in = False
    for win in x_wins:
        if xis in win:
            x_in = True
            win = win.replace(xis, '')
            win = win.split(',')
            ois += [i for i in win if i] 
    if not x_in:
        bi = getIntex(x_xombination, 'b')
        ois += bi 
    return set(ois)

    
all_x_combinations = []
for s in ts:
    all_x_combinations += sorted(list(set(permutations(s))))

final_list = []

for x_xombination in all_x_combinations:
    print(x_xombination)
    xis_in = ','.join(getIntex(x_xombination, 'x'))
    ois_in = ','.join(getIntex(x_xombination, 'o'))
    if isXWins(xis_in): continue
    ois = getOiList(x_xombination)
    for oi in ois:
        final_list.append(list(x_xombination) + [f'x={xis_in}; o={ois_in}'] + [oi])

filename = "test_v3.csv"
    
with open(filename, 'w', newline='', encoding='utf-8') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow([0, 1, 2, 3, 4, 5, 6, 7, 8, 'd', 'o'])
    csvwriter.writerows(final_list) 
# %%
