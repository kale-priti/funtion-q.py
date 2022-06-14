
# Q17. Write a function to tell user if he/she is able to vote or not.( Consider 
# minimum age of voting to be 18. )
def age(a):
    if a>=18:
        print("he/she is able to vote.")
    else:
        print("he/she is not able to vote.")
a=int(input("enter:"))
age(a)