a = {1,3,5,7,9}
from itertools import combinations
comb = list(combinations(a,4))
print(comb)
b = []
for i in comb:
    s1 = 0
    for j in i:
       s1 +=j
    b.append(s1)
big = smol = b[0]
for i in b:
    if big<i:
        big=i
    if smol>i:
        smol = i
print(big)
print(smol)
