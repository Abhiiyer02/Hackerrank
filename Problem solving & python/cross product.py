from itertools import product
p1 = list(map(int,input().split(' ')))
p2 = list(map(int,input().split(' ')))
for i in product(p1,p2):
    print(i,end=' ')