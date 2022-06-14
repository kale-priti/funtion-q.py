# def a():
#     i=1
#     while i<=2:
#         print("who is the founder of the google ")
#         print("-Mark Zuckerberg")
#         print("- Bill Gates")
#         print("- Steve Jobs")
#         print("- Larry Page")
#         i+=1
# print("bubul")        


# Use the add_numbers function given in Part 1 to count 2 integers
#  that have the same position.


# def take_list(a,b):
#     for i in a:
#         for j in b:
#             print(i+j)
# take_list([10,20,30],[80,70,56])













    ###3 no argument with return #####
# def sum():
# 
#     k=3+4
#     return k
# print(sum())


a="a3b6p3"
# adbhps#



# print("Enter a String: ", end="")
# text = input()
# textlength = len(text)
# for char in text:
#     ascii = ord(char)
#     print(char, "\t", ascii)


i=0
k=a[0]
add=""
while i<len(a):
    if a[i]>="1" and a[i]<="9":
        # h=int(a[i])
        ascii=ord(k)
        p=ascii+int(a[i])
        add+=chr(p)
    if a[i]>="a" and a[i]<="z":
        k=a[i]
        add+=k
    i=i+1
print(add)
    