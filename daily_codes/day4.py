import csv
data = [
    ["name ","age","country"],
    ["abc","30","india"],
    ["def","22","bharat"],
    ["ghi","24","america"]
]
with open("data.csv","w",newline="")as file:
    writer = csv.writer(file)
    for x in data:
        writer.writerow(x)
#------------------------------------------------------
try:
    n1=int(input("enter any number"))
    y=25/n1
    print(y)
except ZeroDivisionError:
      print("Division by zero")
#-------------------------------------------------------------------------
