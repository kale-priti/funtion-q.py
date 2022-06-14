# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
def cheak(n):
    i=1
    c=0
    while i <=n:
        if n%i==0:
            c+=1
        i=i+1
    if c<=2:
        print("prime")
    else:
        print("not prime")        
cheak(n=int(input("enter the num")))