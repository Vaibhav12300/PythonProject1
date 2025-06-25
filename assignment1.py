name = input("Enter the student's name: ")
stu_class = input("Enter the student's class: ")
print("Enter marks of five subjects (out of 100):")
marks = []
for i in range(1, 6):
    mark = float(input(f"Subject {i} marks: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
print(f"Name      : {name}")
print(f"Class     : {stu_class}")
print(f"Percentage: {percentage:.3f}%")


#------------------------------------------------------
str1 =input("enter first string:")
str2 = input("enter second string:")
res = str1 + str2
print(res)
print("Uppercase     :", res.upper())
print("Lowercase     :", res.lower())
print("Title case    :", res.title())
print("Length        :", len(res))
print("Reversed      :", res[::-1])


#-------------------------------------------------------------
print("Hello, World!")
print("Welcome", "to", "Python")
print("hello python",'welcome',6,sep=";",end="---")
print("hello")
print("hello")
name = "Vaibhav"
print("Hello", name)

#--------------------------------------------------------------
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
if num2 != 0:
    div = num1 / num2
    mod = num1 % num2
else:
    div = "Cannot divide by zero"
    mod = "Cannot perform modulus with zero"
print("\n--- Calculator Results ---")
print(f"Addition       : {add}")
print(f"Subtraction    : {sub}")
print(f"Multiplication : {mul}")
print(f"Division       : {div}")
print(f"Modulus        : {mod}")






