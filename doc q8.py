# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12


def string(a):
    i=0
    lower_c=0
    upper_c=0
    while i<len(a):
        if a[i]>="a" and a[i]<="z":
            lower_c+=1
        if a[i]>="A" and a[i]<="Z":
            upper_c+=1
        i=i+1
    print(upper_c)
    print(lower_c)
string('The quick Brow Fox')