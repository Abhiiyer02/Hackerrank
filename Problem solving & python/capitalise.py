word = input()
def split(word):
    return [char for char in word]
def upp(list):
    for i in range (len(list)):
        print(list[i].isupper)

        i+=1

x = split(word)
list1 = list()
for i in x:
    if i.isupper():
        print('true')

