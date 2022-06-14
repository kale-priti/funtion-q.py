# def factorial(n):
# 	    if n == 0:
# 	        print(1)
# 	    else:
# 	        print(n *(n-1))

# factorial(n=int(input("Input a number to compute the factiorial : ")))


# a=input("enter:")
# d=a[::-1]
# if a==d:
# 	print("palidrom")
# else:
# 	print("not palidrom")

a=[[1,2],[1,2,3,4],[1],[1,2,3,4,5]]
i=0
max=[]
min=a[0]
while i<len(a):
	if len(a[i])>len(max):
		max=a[i]
	if len(a[i])<len(min):
		min=a[i]
	i=i+1
print(len(min),min)
print(len(max),max)
