# Q9.Write a Python program to generate and print a list of first and last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).
# def renge(a,b):
#     i=a
#     k=[]
#     while i<=5:
#         s=i**2
#         k.append(s)
#         i=i+1
#     print(k)
#     j=b-4
#     c=[]
#     while j<b:
#         l=j**2
#         c.append(l)
#         j=j+1
#     print(c)
# renge(1,30)


def square(a):
    i=1
    l=[]
    l1=[]
    while i<=(a):
        if i>0 and i<6:
            l.append(i**2)
        elif i>25 and i<=30:
            l1.append(i**2)
        i+=1
    print((l,l1))  
square(30)

