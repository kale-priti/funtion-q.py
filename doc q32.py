# Q32.Complete the function that takes a non-negative integer n as input, and 
# returns a list of all the powers of 2 with the exponent ranging from 0 to n 
# (inclusive). 
# n=0 == >[1]   #[2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2].
def num(a):
    i=0
    b=[]
    while i<=2+1:
        b.append(a*i)
        print(b)
        i=i+1
a=int(input("enter:"))
num(a)




