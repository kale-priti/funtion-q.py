# # [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# # [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)


# def num(a):
#     max=0
#     sec_max=0
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(a):
#            if a[j]>max:
#                max=a[j]
#            if a[j]>sec_max and a[j]!=max:
#              sec_max=a[j]
#            j+=1  
#         i=i+1
#     print(max)
#     print(sec_max)

# num([10, 14, 2, 23, 19])  


# py_list = ['Python', 2, 'Pythö', 3]
# print(ascii(py_list))


a=[2,3,4,5,6,7,8]
#[2,3,3,4,4,5,5,6,6,7,7,8]
i=0
b=[]
while i<len(a):
    j=0
    while j<=i+1:
        b.append(a[i])
        j=j+1
    i=i+1
print(b)

