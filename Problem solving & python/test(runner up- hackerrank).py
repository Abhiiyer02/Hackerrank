n = int(input())
list1 = list(map(int, input().split()))
list1.sort()
list2 = list(set(list1))
max2 = list2[-2]
print(max2)
#res = []
#j=min(list1)
#while j<max(list1) :
    #if j not in res:
        #res.append(j)
        #j += 1
#print(res)
#max1 = max((list2))
#print(list2)
#for i in list1:
    #if i == max1:
      #  i+=1

#max2= max(list1)
#print(max2)

