
# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
# generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]
# Note

def renge(a,b,d):
    k=[]
    i=a
    while i<=b:
        k.append(i)
        i=i+d
    print(k)
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
renge(a,b,c)