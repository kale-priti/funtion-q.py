# Q46. Draw a flowchart to take a list of N numbers from the user, print True 
# if the complete list consists of consecutive numbers with a difference of one.
#  Print False otherwise. 
def name(a):
    a=[1 ,2, 3, 4, 5, 8, 7]
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
    if c==len(b):
        print("true")
    else:
        print("false")
name([2,4,5,7,8])


# def my_function(**kid):
#       print("His last name is " + kid["fname"])

# my_function(fname = "Tobias", lname = "Refsnes") 


# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# 

