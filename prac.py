# a=[1,2,3,4]
# b=[1,8,9,6,2,14,4]
# i=0
# k=[]
# while i<len(a):
#     if a[i] not in b and a[i] not in k:
#         k.append(a[i])
#     j=0
#     while j<len(b):
#         if b[j] not in a and b[j] not in k:
#             k.append(b[j])
#         j=j+1
#     i=i+1
# print(k)
# print(sorted(k))

a="my name is priti"
b=a.split()
print(len(b))
i=0
s=""
while i<len(b):
    if b[i][0]:
        k=b[i][0].upper()
        s=s+k
    j=1
    while j<len(b[i]):
        s+=b[i][j]
        j=j+1
    i=i+1
print(s)



#     j=0
#     l=""
#     while j<len(b[i]):
#         if b[j][0]:
#             k=b[j][0].upper()
#             l=l+k
#         else:
#             k=b[j]
#             l=l+k
#         j=j+1
# print(l)    


# a=["this","is","amazing","day"]
# i=0
# b=[]
# while i<len(a):
#     if i%2==0:
#         b.append(a[i][::-1])
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)