
n = input()
a=0
b=0

for i in range (int(n)):
    p = list(map(str,input().split()))
    a = int(p[0])
    b = int(p[-1])
    if(a==0):
        print("1")
    elif a!=0 :
        if b == 0:
            print(a+1)
        if b!=0:
            print(a+(2*b)+1)