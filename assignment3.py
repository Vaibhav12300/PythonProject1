def basic_operations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b if b != 0 else "Cannot divide by zero"
    return add, sub, mul, div
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition, subtraction, multiplication, division = basic_operations(num1, num2)
print("\n--- Math Operation Results ---")
print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division       : {division}")


#----------------------------------------------------------------------------------


num = int(input("Enter a number: "))
original_num = num
reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10
if original_num == reverse_num:
    print(f"{original_num} is a Palindrome Number.")
else:
    print(f"{original_num} is NOT a Palindrome Number.")
