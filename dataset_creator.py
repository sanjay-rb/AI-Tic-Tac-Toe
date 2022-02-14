# %% [markdown]
# ## Import Libraries 

# %%
from itertools import permutations
import csv

# %% [markdown]
# ## All possible XO base combinations

# %%
base_combinations = [
    'xbbbbbbbb',
    'xoxbbbbbb',
    'xoxoxbbbb',
    'xoxoxoxbb',
    'xoxoxoxox',
]

# %% [markdown]
# ## Define variable called final list to write in 

# %%
final_list = []
filename = "tic-tac-toe.csv"

# %% [markdown]
# ## Find all XO combinations from the base combinations

# %%
all_x_combinations = []
for s in base_combinations:
    all_x_combinations += sorted(list(set(permutations(s))))

# %% [markdown]
# ## All possible X wins states

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

# %% [markdown]
# ## Function to get all index if character from the list as an array

# %%
def getIntex(l, v):
    indices = []
    for i in enumerate(l):
        if i[1] == v:
            indices.append(str(i[0]))
    return sorted(indices)

# %% [markdown]
# ## Function to check whether given X combinations is won for X

# %%
def isXWins(x_xombination):
    xi = ','.join(getIntex(x_xombination, 'x'))
    for win in x_wins:
        if win in xi or win == xi:
            return True
    return False

# %% [markdown]
# ## Function to get list of possible O places from X combinations
# ### Algorithm
# - ✔️ Check whether given X combination is having subset of X wins
#     1. Replace X combination subset from the X wins and set remaining X position to O
# - ✔️ If X combination not in X wins
#     1. Get blank space index and set to O 

# %%
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

# %% [markdown]
# ## Script to populate final list with correct values

# %%
for x_xombination in all_x_combinations:
    print(x_xombination)
    current_x_index = ','.join(getIntex(x_xombination, 'x'))
    current_o_index = ','.join(getIntex(x_xombination, 'o'))
    if isXWins(x_xombination): continue
    ois = getOiList(x_xombination)
    for oi in ois:
        if current_o_index:
            final_list.append(list(x_xombination) + [f'x={current_x_index}; o={current_o_index}'] + [oi])
        final_list.append(list(x_xombination) + [f'x={current_x_index}'] + [oi])

# %% [markdown]
# ## Create CSV from the final list 

# %%
with open(filename, 'w', newline='', encoding='utf-8') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(["Box 0", "Box 1", "Box 2", "Box 3", "Box 4", "Box 5", "Box 6", "BOx 7", "Box 8", "Description", "O's Move"])
    csvwriter.writerows(final_list) 


