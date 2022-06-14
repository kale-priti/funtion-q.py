# 10. Write a Python program to print the even numbers from a given list. Go to the editor
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def n(num):
    b=[]
    # i=0
    # while i<len(num):
    #     if num[i]%2==0:
    #         b.append(num[i])
    #     i=i+1
    
    
#     for i in range(len(num)):
#         if num[i]%2==0:
#             b.append(num[i])
#     print(b)
# n([1, 2, 3, 4, 5, 6, 7, 8, 9])



import random 
import string
# alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'
# ,'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
# '0','1','2','3','4','5','6','7','8','9',"!","@","#","$","&",]
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbol=string.punctuation
sum=lower+upper+digit+symbol
b=[]
b.append(sum)
pas=int(input("enter the len"))
i=0
pasw=""
while i<pas:
    password=random.shuffle(b)
    pasw="",password
    i=i+1
print(pasw)