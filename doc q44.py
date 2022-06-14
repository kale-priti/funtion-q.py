
# Q44.Bonus - Given the same list, print the last ‘N’ elements in reverse order.
# Sample Input:
# 2
# Sample Output:
# q
# b 
# Sample Input:
# 3
# Sample Output:
# q
# b 
# 5

def l(k):
    a=int(input("enter:"))
    i=1
    while i<=a:
        print(k[-i])
        i=i+1
l(['a',1,'2',5,'b','q']  )