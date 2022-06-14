
# Q42. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
def l(a):
    i=0
    b=[]
    while i<len(a):
        k=str(a[i])
        sum=0
        j=0
        while j<len(k):
            sum=sum+int(k[j])
            j=j+1
        b.append(sum)
        i=i+1
    print(b)
l([12, 67, 98, 34])



def l(a):
    b=[]
    for i in a:
        k=str(i)
        sum=0
        for j in k:
            sum=sum+int(j)
        b.append(sum)
    print(b)
l([15, 81, 11, 234])
            