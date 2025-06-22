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
per = int(input("percentage?:"))
if per > 60:
    print("grade A")
elif per > 50:
    print("grade B")
elif per >40:
    print("grade C")
else:
    print("grade D")
#-----------------------------------------------------------------------------------------
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"The factorial of {num} is {factorial}.")
#---------------------------------------------------------------------------------
l=[10,5,6,20,45]
n=len(l)
l.sort()
print(l)
print(f"smallest no is {l[0]}")
print(f"second smallest number is {l[1]}")
print(f"second greatest number is {l[n-2]}")
#------------------------------------------------------------------------------------
items = []
prices = []

while True:
    print("\n===== Billing Menu =====")
    print("1. Create Bill (Add Item)")
    print("2. Display Item Prices and Total")
    print("3. Display Total Only")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter item name: ")
        price = float(input("Enter item price: ₹"))
        items.append(name)
        prices.append(price)
        print(f"Item '{name}' added to the bill.")

    elif choice == '2':
        if not items:
            print("No items added yet.")
        else:
            print("\n--- Bill Details ---")
            for i in range(len(items)):
                print(f"{items[i]} : ₹{prices[i]:.2f}")
            print(f"Total Amount: ₹{sum(prices):.2f}")

    elif choice == '3':
        print(f"Total Amount: ₹{sum(prices):.2f}" if prices else "No items added yet.")

    elif choice == '4':
        print("Exiting the billing system. Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
