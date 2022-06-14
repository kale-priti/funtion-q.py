
# 4. Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


def str_reverse(str1):
    rev=""
    i=len(str1)
    while i>0:
        rev=rev+str1[i-1]
        i=i-1
    print(rev)
str_reverse("1234abcd")

