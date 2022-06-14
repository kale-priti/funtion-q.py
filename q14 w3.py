# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow


def so(string):
    string = string.split("-")
    string.sort()
    print('-'.join(string))

so("green-red-black-white ")
