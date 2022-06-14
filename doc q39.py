# Q39. Your task is to make two functions, max and min (maximum and minimum in PHP 
# and Python, maxi and mini in Julia) that take a(n) array/vector of integers list 
# as input and outputs, respectively, the largest and lowest number in that array/
# vector.
# #Examples:-

def name(a):
    max=0
    min=a[0]
    i=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        if a[i]<min:
            min=a[i]
        i=i+1
    print(max)
    print(min)
name([42, 54, 65, 87, 0])