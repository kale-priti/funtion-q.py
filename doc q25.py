
# Q25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

def count(a):
    pos=0
    neg=0
    i=0
    while i<len(a):
        if a[i]>=0 :
            pos+=1
        else:
            neg+=1
        i=i+1
    print("pos-",pos,",","neg-",neg)
count([2, -7, 5, -64, -14])