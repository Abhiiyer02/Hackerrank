list1 = list(map(int ,input().split()))
n = list1[0]
a= list1[1]
b = list1[2]
seq= list(map(int, input().split()))
deny_count=0
deny_count2=0
for i in seq:
    if i ==2 :
        b-= 1

        if b==0:
            deny_count+= 2
for i in seq:
    if i==1 :
        a-=1
        count2 =0
        if a== 0:
            b-=1
            count2+=1
            if count2>float(b/2):
              deny_count2+=1
no_of_people_denied= int(deny_count)+ int(deny_count2)-1
print(no_of_people_denied)

