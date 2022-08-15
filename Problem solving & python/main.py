year= int(input("Enter year "))
leap= True
if (year%4==0 and year%100!=0) or year%400 == 0:
        print(leap)
else:
    leap = False
    print(leap)
