
# Q5.Write a Python function that takes a list and returns a new list with unique 
# elements of the first list.

def unique(a):
    b=[]
    i=0
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        i=i+1
    print(b)
unique([1,5,8,1,8,4,])

