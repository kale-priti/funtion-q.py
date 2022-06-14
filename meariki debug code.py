# def sum():
#     print(12+13)
# sum()

# def even():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# even()


# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Aatif")

# def add_numbers(num1, num2):
#     print("I will add two numbers.")
#     print(num1 + num2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)



# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")


# def icecream(*flavours):
#      for flavour in flavours:
#          print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")



# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")


# def greet(names):
#     for name in names:
#         print("Welcome", name)

# greet(["Rinki","Vishal", "Kartik", "Bijender"])
# greet("Rinki")
# greet("Vishal")
# greet("Kartik")
# greet("Bijender")


# def info(name, age="21"):
#     print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")



# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("priti", "list", "monika")

# Write a function named function_print_lines which takes 2 strings, and prints 
# them in the following manner.

# If we give these 2 arguments - "My name is Rishabh." and "I am the co-founder 
# of NavGurukul"
# we will get the following output:


# def name(nam,x):
#     print("my name is",nam,".")
#     print("i am a founder of ",x)
# name("larry page","google")


# You have to define a function named isGreaterThan20 in which you have to pass 
# two parameters to the function and the first parameter by default should be 20.

# def isgreaterthen20(a,b=20):
#     if a>b:
#         print("a is greater then b")
#     else:
#         print("b is greater then a")
# isgreaterthen20(40)


# Write add_numbers function here
# def add_numbers(a,b):
#     print(a+b)
# add_numbers(10,28)


# print("NavGurukul")

# def say_hello():
#     print("Hello!")
#     print("How are you?")

# say_hello()
# print("Python is awesome")
# say_hello()
# print("Hello…")
# say_hello()



# def definition_say_hello():
#     print("NavGurukul")
#     print("In Navgurukul, we have to take responsibility for our learning.")

# definition_say_hello()

# print("In Navgurukul we treat all the people in the same way.")

# definition_say_hello()




# def function_say_bye():
#     print("It was fun meeting with you. ")
#     print("Bye bye")
# function_say_bye()
# function_say_bye()
# print("Python is used a lot.")
# function_say_bye()
# function_say_bye()





# def definition_hello_again():
#     print("Again Hello :)")
#     print("How are you?")
# definition_hello_again()


# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot(406)




# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number//=10
#         return sum
# print(sumofdigits(123))



# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))


def checkKey():
    car ={"brand":  "ford","model":  "mustang","year":  1964}
    if "model"in car:
        print("Yes, model is one of the keys in the thisdict dictionary.")
    else:
        print("No, 'model' key dictionary mai nahi hai.")
checkKey()