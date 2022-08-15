number_of_problems = int(input())

for i in range (0,number_of_problems):
    ele= list(map(int , input().split()))
    count = 0
    for i in ele:
        if i == 1:
            count += 1
            solvable = 0
            for i in ele :
                if count == 2:
                    solvable += 1

print(solvable)

