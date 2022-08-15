import string
t12 = list(input())
if t12[-2] == 'A':
    if t12[0] == '1' and t12[1] == '2':
        t12[0] = t12[1] = '0'
else:
    import array as arr
    temp = arr.array('i', [])
    j = 0
    for i in t12:
        temp.append(int(i))
        j += 1
        if j == 2:
            break
    if temp[0] == 1:
        if temp[1] == 2:
            x = 0
        else:
            temp[0] += 1
            temp[1] += 2
    elif temp[0] == 0:
        temp[0] = 1
        temp[1] += 2
        if temp[1] > 7:
            temp[0] = 2
            temp[1] = (temp[1]) % 10

    t12[0] = temp[0]
    t12[1] = temp[1]
t12.pop(-1)
t12.pop(-1)
t24 = " "
for i in t12:
    print(i, end="")
t24 = str(t12)
print(t24)
y = t24.join(t12)
print(y)