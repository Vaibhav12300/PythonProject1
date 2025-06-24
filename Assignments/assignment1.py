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





