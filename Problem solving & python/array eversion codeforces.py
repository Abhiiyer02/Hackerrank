n = int(input())
for j in range(n):
    size = int(input())
    a = list(map(int, input().split()))
    a1 = []
    a2 = []
    a3 = a
    count = 0
    while 1:
        for i in a3:
            if i <= a3[-1]:
                a1.append(i)
            if i > a3[-1]:
                a2.append(i)
        if a3 == a1 + a2:
            break
        else:
            count += 1
        a3.clear()
        a3 = a1 + a2

        a1.clear()
        a2.clear()
    print(count)
