# Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
def creat():
    i=1
    while i<=10:
        num=int(input("enter the num:"))
        if num%2==0:
            print(num*100)
        else:
            print(num*-1)
        i=i+1
creat()