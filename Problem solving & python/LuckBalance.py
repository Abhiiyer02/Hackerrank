n = int(input())
k = int(input())
contests = []
for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))
contests.sort()
luck = 0
l1=[]
l0=[]
for i in contests:
    if i[-1] == 0:
        l0.append(i)
    else:
        l1.append(i)
l1.sort()
print(contests)
print(l1)
print(l0[-1][0])
for i in l0:
    luck += i[0]
for i in range(k):
    luck += l1[-1][-2]
    l1.pop(-1)
for i in l1:
    luck -= i[0]
print(luck)

