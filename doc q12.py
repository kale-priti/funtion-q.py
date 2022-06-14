
# Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# -1050 -> -105

def num(a):
    while a>=0 :
        if a%10!=0:
            print(a)
        a=a//10
a=int(input("enter:"))
num(a)
