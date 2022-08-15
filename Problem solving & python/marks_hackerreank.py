scores1 = set()
markslist= []
list2= []
for i in range(int(input())) :
   name = (input())
   score = float(input())
   markslist.append([name,score])
   scores1.add(score)
min2 = sorted(scores1)[1]

for name,score in markslist:
   if score == min2:
      list2.append(name)

for name in sorted(list2) :
      print(name,end='\n')
0