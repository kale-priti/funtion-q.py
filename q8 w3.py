# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
# Sample List :[1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unic(a):
    i=0
    b=[]
    while i<len(a):
        j=i+1
        while j<len(a):
            if a[i]!=a[j]:
                b.append(a[i])
            j=j+1
        i=i+1
    print(b)
unic([1,2,3,3,3,3,4,5])
