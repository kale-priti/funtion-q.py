# Q49. Write a flowchart which takes an input N. Then input N numbers. Then for each
#  of the N numbers, print “even” if the number is even or and “odd” if the number is
#   odd.
def num():
    a=int(input("enter:"))
    i=0
    while i<a:
        a=int(input("enter the num:"))
        if a%2==0:
            print("even")
        else:
            print("odd")
        i=i+1
num()