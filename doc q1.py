# Q1.Write a Python program to count the number of strings where the string 
# length is 2     or more and the first and last characters are the same from a 
# given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']
# result= 2.

a=['aba', 'xyz', 'aba', '1221']
c=0
for i in a:
    if len(i)>=2 and i[0]==i[-1]:
        c+=1
print(c)
