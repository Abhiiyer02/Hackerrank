no = int(input())
for i in range(2,no):
    if no%i ==0:
        print("not prime")
        break
else :
    print("prime")