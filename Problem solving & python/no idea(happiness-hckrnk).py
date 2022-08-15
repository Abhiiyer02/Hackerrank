n =  input().split(' ')
arrr = input().split(' ')
set_a = set(input().split())
set_b = set(input().split())
#print(sum((i in set_a)-(i in set_b) for i in arrr))
hap = 0
for i in arrr:
    if i in set_a:
            hap += 1
    if i in  set_b:
            hap -= 1
print(hap)
