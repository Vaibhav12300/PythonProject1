# d={1:"python",2:"java",'name':"programming language",4:{1:"one",2:'two'}}
# print(d[4])
# print(type)
#------------------------
# Dict = {}
# print(Dict)
# Dict[0]='python'
# Dict[2]='java'
# print(Dict)
#-----------------------------
dict1 = {1:"python",2:"java",3:"c++",4:"dart"}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
dict2.items()
print(dict2.items())
dict2.keys()
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
print(dict2.values())

#------------merge two dictionary-----------------------------
dict1={'a':10,'b':8}
dict2={'d':6,'c':4}
dict1.update(dict2)
print(dict1)
#-----------stack------------------------------
# l = []
# while True:
#     c = int(input('''
#     1.Insert element
#     2.Pop element
#     3.Peek element
#     4.Display stack
#     5.Exit
# '''))
#     if c == 1:
#         n = input("Enter value: ")
#      l.append(n)
#     print(l)
#     elif c == 2:
#     if len(l) == 0:
#         print("empty stack")
#     else:
#         p = l.pop()
#         print(p)
#         print(l)
#     elif c == 3:
# if len(l) == 0:
#     print("empty stack")
#     else:
#     print("Last stack value: ", l[-1])
#     elif c == 4:
#     print(l)
#     elif c == 5:
#     break
#     else:
#         print("Invalid input!!!")
#----------------------tuple------------------------------------------------
t = (10,20,30,40,50)
print(t)
print(type(t))
l = len(t)
for x in range(l):
    print(t[x])
#--------------------nested tuple---------------------------
# t1=(0,1,2,3)
# t2=('a','b')
# t3=(t1,t2)
# print(t3)
# #--------------repetition in tuple---------------------
# t=('xyz',)*3
# print(t)
#-----------------------------
t= (0 ,1, 2, 3)
print(t[1:])
print(t[::-1])
print(t[2:4])
print(t[2:3])
#----------------------------------
#t=(0,1)
#del t
#print(t)
#-------------------------
l=[10,20,3,6,44]
t = tuple(l)
print(t)
print(len(l))
print(min(t))
print(max(t))
print(t.count(10))
print(t.index(20))
print(sum(t))
#-----------sets-----------------
s = {"a","b","c","d","e"}
s.add("f")
print(s)
#--------------------------------
s = {"apple", "banana", "cherry", True, 1, 2, False, 0}
print(s)
#----------------------------------------------------------
# s1={"car","bike","ship"}
# s2={"watch","land","water"}
# s3=s1.union(s2)
# print(s3)
# s4=s1|s2
# print(s4)
# #----------------------------------
s11=set()
s22=set()
for i in range(5):
    s11.add(i)
for i in range(3,9):
    s22.add(i)
    s33=s11.intersection(s22)
    print(s33)
#------------------------------------------
    s1 = {1, 2, 3, 4, 5, 6}
    print(s1)
    s1.clear()
    print(s1)
#-------------function--------------------------
# def my_fun(a=0,b=0):
#     print("sum",a+b)
#     res=a+b
#     return res
# my_fun(12,15)
# #----------------------------------------------------
# def my_fun(*city):
#     print(city[1])
# my_fun("a","b","c")
# #------------------------------------------
# def my_fun(*city):
#     print(city[2])
# my_fun("a","b","c")
# #-----------------file------------------------
# f = open("new1.txt","w")
# f.write("this is my first line")
# f.write("this is second line")
# f.close()
# #---------------------------------------------
# f=open("new1.txt","r")
# #for x in f:
#  #   print(x)
# print(f.read())
# #----------------------------------------------------
# d = {1: "python", 2: "java", 3: "C++", "name": "Program"}
# print(d['name'])
# print(d[1])
# #----------------------------------------------------------
# d= {1: 'Program', 2: 'For', 3: {'A': 'Dictionary', 'B': 'In', 'C': 'Python'}}
# print(d)
# print(d[1])
# print(d[3]['A'])
#
#
#
#
