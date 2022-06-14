# import random 
# import string
# # # alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'
# # # ,'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
# # # '0','1','2','3','4','5','6','7','8','9',"!","@","#","$","&",]
# # pas=int(input("enter the len"))
# lower=string.ascii_lowercase
# upper=string.ascii_uppercase
# digit=string.digits
# symbol=string.punctuation
# abc=[]
# abc.append(lower)
# abc.append(upper)
# abc.append(digit)
# abc.append(symbol)
# # print(abc)
i=0
lenth=int(input("enter the num:"))
while i<len(abc):
    j=0
    pasw=""
    while j<lenth:
        password=random.choice(abc(sum))
        pasw="".password
        j=j+1
    i=i+1
print(pasw)


# import random
# import string
# lower=string.ascii_lowercase
# upper=string.ascii_uppercase
# digit=string.digits
# symbol=string.punctuation
# sum=lower+upper+digit+symbol
# lenth=int(input("enter the lenth"))
# b=[]
# sum=lower+upper+digit+symbol
# b.append(sum)
# print(b)
# i=0
# while i<lenth:
#     k=random.shuffle(sum)
#     password="".join(k)
# print(password)
