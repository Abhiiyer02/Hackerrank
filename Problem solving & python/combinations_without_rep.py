from itertools import combinations
l,n= list(map(str,input().split(" ")))

for i in range (int(n)):
    for i in combinations(sorted(l),i):
        print(''.join(i))