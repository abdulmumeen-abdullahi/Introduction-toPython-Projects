import math
#
print("This is a program that can solve any quadratic equation using Mathe Modules")
a=input("Enter the value of a: ")
b=input("Enter the value of b: ")
c=input("Enter the value of c: ")
z1=(-int(b)+(math.sqrt((math.pow(int(b),2))-(4*int(a)*int(c)))))/(2*int(a))
z2=(-int(b)-(math.sqrt((math.pow(int(b),2))-(4*int(a)*int(c)))))/(2*int(a))
print("The answer for the quadratic equation are: ", "z1= ",z1, "and " "z2= ",z2)