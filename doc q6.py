# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].

# a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(a):
    k=[]
    for i in a:
        if i%2==0:
            k.append(i)
    print(k)
even([1, 2, 3, 4, 5, 6, 7, 8, 9])