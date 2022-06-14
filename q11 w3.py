

# 11. Write a Python function to check whether a number is perfect or not. Go to the editor
# According to Wikipedia : In number theory, a perfect number is a positive integer that is 
# equal to the sum of its proper positive divisors, that is, the sum of its positive divisors 
# excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number 
# is a number that is half the sum of all of its positive divisors (including itself).
def num(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=i
        i=i+1
    if a==n:
        print("prefect")
    else:
        print("not")
num(n=int(input("enter the num")))