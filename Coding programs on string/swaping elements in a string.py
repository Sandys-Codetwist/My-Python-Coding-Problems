def swapping(x):
    x[2],x[1]=x[1],x[2] #list is accesed by the index so, we can swap list element by using index
    return x
print(swapping([1,2,3]))

