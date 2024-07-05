print("Program to convert base 10 numbers to base 2")
x=input("Enter any base 10 number: ")
y=bin(int(x))
print("The conversion of the number you entered to base 2 is ", y,
      "\n")
#Program to convert base 2 numbers to base 10
a=input("Enter any base 2 number: ")
v=bin(int(a))
d=int((v))
print("The conversion of the number you entered to base 10 is ", d)
#I guess the program above won't be able to convert base 2 numbers to base 10 since all input values are recorded as integer, not binary number.")"""
#
print("This is a program to convert base 10 numbers to base 8")
h=input("Enter any number: ")
v=oct(int(h))
print("The conversion of the number you entered to base 8 is ", v,
      "\n")
#
print("Program to convert base 10 numbers to base 16")
u=input("Enter any number: ")
t=hex(int(u))
print("The conversion of the number you entered to base 16 is ", t)
#
print("This program is to convert various number types.")
#
print("This is a program to convert a decimal number to an integer form")
a=input("Enter any decimal number: ")
b=int(float(a))
print("The decimal number has been converted to an integer value of ", b)
#
print("This is a program to convert integer numbers to complex form")
c=input("Enter the integer value of c: ")
k=input("Enter the integer value of k: ")
d=complex(int(c),int(k))
print("The complex form of the integer numbers is ", d)
#
# ----------------------------This program uses number conversion principle and class type to confirm the result gotten
print("This is a program to convert an integer number to a string form") # string value is a value stores inside ""
p=input("Enter any integer number: ")
r=str(int(p))
print("The string value of the integer input is ",r)
s=(type(r))
print("The class type is ",s)
#
print("This is a program to convert a string form to an integer number")
v=input("Enter any string value: ")
i=int(str(v))
print("The integer number of the string value input is ",i)
j=(type(i))
print("The class type is ",j)
#
print("This is a program to convert a string form to a tuple form")
q=input("Enter any string value: ")
w=tuple(str(q))
print("The tuple form of the string value input is ",w)
e=(type(w))
print("The class type is ",e)
#
print("This is a program to convert a string form to list form")
r=input("Enter any string value: ")
t=list(str(r))
print("The list form of the string value input is ",t)
y=(type(t))
print("The class type is ",y)
#
print("This is a program to convert a string form to set form")
u=input("Enter any string value: ")
i=set(str(u))
print("The set form of the string value input is ",i)
o=(type(i))
print("The class type is ",o)