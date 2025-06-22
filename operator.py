a = 100
b = 30
result = (a+b)/2
print(result)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
#--------------------------
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)
#-------------------------
a = 100
b = 10
if a is b:
    print(a)
#=====
str = "python"
if "p" in str:
    print(str)
    #-----------------------
    a = 10
    b = 8
    print(bin(a))
    print(bin(b))
    print(a&b)
    #-------------------------------------
    n1 = int(input("enter any number:"))
    if n1%2==0:
        print("number is even")
    else:
        print("number is odd")
#--------------------------------------------
per = int(input("percentage?:"))
if per > 60:
    print("grade A")
elif per > 50:
    print("grade B")
elif per >40:
    print("grade C")
else:
    print("grade D")
#--------------------------------
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
operation = input("enter operation (+,-,*,/,%)")
                  if operation == "+":
                      res = n1+n2
                  elif operation == "-":
                      res = n1-n2
                  elif operation == "*":




