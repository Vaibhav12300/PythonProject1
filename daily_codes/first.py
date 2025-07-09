# print("hello python",'welcome',6,sep=";",end="---")
# print("hello")
# print("hello")
# a=10
# b=8
# print(f"the sum of {a} and {b} is :",a+b,sep=";")
# print(9>7)
# print("vaibhav gupta")
# c=("Vaibhav is a good boy")
# d=("Somya is a bad boy")
# print(f"{c} and {d}")
# print(f"the value of pi is{22/7:.9f}")
# #a = int(input("enter any number:"))
# #print(a+4)
# #a = int(input("enter value of a"))
# #print(a)
# #b = int(input("enter value of b"))
# #print(b)
# #print(f"multiplication of {a} and {b} is ",a*b)
# a = "hello"
# b = "world"
# print(a+b)
# a = "this is python"
# print(a.expandtabs(40))
# str = " this is python"
# print(str.replace( "is", "is great"))
# str1 = " Names:\nA\nB\nC\nD"
# print("String before splitting:"+str1)
# print("string after splitting:")
# print(str1.splitlines())
# t = "tipon"
# e = "12345"
# str = " this is python!!!"
# encoding = str.maketrans(t,e)
# print(str.translate(encoding))
# #n = int(input("how many box"))
# #print(n)
# print('09', '12', '2016', sep='-')
# print('09-12-2016')
#
# print("Python", end='@')
# print("hello")
# x = 50
# y = 10
# print(input("enter x "))
# print(x)
# print(input("enter y"))
# print(y)
# print(f"division of {x} and {y} is :",x/y)
# name = 'Tushar'
# age = 23
# print(f"Hello, My name is {name} and I'm {age} years old.")

# Prompting the user for input
age_input = input("Enter your age: ")

# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
#------------------------------------------------------------------
str="this is python!!!"
print(str.rpartition(" "))