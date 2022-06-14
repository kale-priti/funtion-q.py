# Q3.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20.
def sum(a):
    add=0
    i=0
    while i<len(a):
        add=add+a[i]
        i=i+1
    print(add)
sum([8, 2, 3, 0, 7])
