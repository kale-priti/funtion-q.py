# Q30. Write a function that prints all the prime numbers between 0 and limit where
#  limit is a parameter.
# def parameter(limit):
#     i=1
#     while i<=limit:
#         j=1
#         c=1
#         while j<i:
#             if i%j==0:
#                 c=c+1
#             j=j+1
#         if c==2:
#             print(i)
#         i=i+1   
# limit=int(input("enter the num:"))
# parameter(limit)
    

def parameter(limit):
    for i in range (0,10):
        c=1
        for j in range (1,i):
            if i%j==0:
                c=c+1
        if c==2:
            print(i)
limit=int(input("enter:"))
parameter(limit)
