print(dir(list))

l=["sand","sanjju","sunny",1,32,3,]
l.append ("titus")
print(l)

l.clear()
print(l)

b=['s','s',1,44,2,4,4,'a',4,5,5,5,5,55,5,'t']
b1=b.count(5)
print(b1)

print(b.copy())
print(b.insert(0,7))

print(b.pop(9))
r=[8,9,5,4,1,2,3]
print(r.remove(5))
print(r.reverse())
print(r.sort())
print(l.extend(l))


def mylist(list):
    list.extend(list)
    return list
L =[1,2,3,4,5]
print(mylist(L))