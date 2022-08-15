from itertools import permutations
l,n= list(map(str,input().split(" ")))
for i in permutations(sorted(l),int(n)):
    print(''.join(i))