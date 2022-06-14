    # Q41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
def lenth(a):
    max=[]
    min=a[0]
    print(len(min))
    i=0
    while i<len(a):
        if len(a[i])<len(min):
            min=a[i]
        if len(a[i])>len(max):
            max=a[i]
        i=i+1
    print(len(min),min)
    print(len(max),max)
lenth([[[0],1, 3], [5, 7], [9, 11], [13, 15, 17]])
        
