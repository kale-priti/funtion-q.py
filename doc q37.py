# Q37. Consider an array/list of sheep where some sheep may be missing from their
#  place. We need a function that counts the number of sheep present in the array 
#  (true means present).
def count(a):
    i=0
    c=0
    while i<len(a):
    
        if a[i]==True:
            c=c+1
        i=i+1
    print(c)
count([True,  True,  True,  False,
True,  True,  True,  True ,
True,  False, True,  False,
True,  False, False, True ,
True,  True,  True,  True ,
False, False, True,  True])