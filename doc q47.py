# Q46. Draw a flowchart to take a list of N numbers from the user, print True if 
# the complete list consists of consecutive numbers with a difference of one. 
# Print False otherwise. 


# Q47. Draw a flowchart to take a list of 7 numbers from the user, print True if the complete list consists of consecutive numbers with any constant difference between numbers. Print False otherwise. 
# Sample Input:
# 2 4 6 8
# Sample Output:
# True
# Sample Input:


# Sample Input:
# 1 2 3 4 5 6 7
# Sample Output:
# True
# Sample Input:
# 45 46 47 48 49 51 52
# Sample Output:
# False
def name(a):
    i=0
    b=[]
    while i<len(a)-1:
        k=a[i+1]-a[i]
        b.append(k)
        i=i+1
    i=0
    k=b[0]
    c=0
    while i<len(b):
        if b[i]==k:
            c=c+1
        i=i+1
    print(len(b))

    if c==len(b):
        print("true")
    else:
        print("false")
   
name([2,4,6,8])