import math
print("This is a program that solve simple arithmetic problems using Mathe Modules and number conversion")
w=input("Enter any negative number: ")
x=(math.pi*abs(int(w)))#math.pi is to input the constant value of pie and abs is to input the absolute value of w
print("The product of pie and the absolute value of ", w, " is ", x, "\n")
#--------------------------------------------------------------------------------------------------------------------
print("This program is going to use variable assignment to convert the values stored")
r=float(input("Enter any decimal number: ")) #The float() enables 'r' to store decimal value
t=math.ceil(r)+math.floor(r) #math.ceil and math.floor convert the input value internally
print("The sum of the next greater whole number of", r, "and its nearest lower whole number is",t, "\n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
i=input("Enter any integer whole number: ")
q=(math.sqrt(math.e*int(i))) #math.sqrt is to find the square root of the product of exponential and the input value of i
print("The product of exponential and the value of ", i, " is ", q, "\n")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
p=input("Enter any decimal number: ")
u=math.e*math.ceil(float(p))*math.floor(float(p)) #math.ceil is to round a decimal number to its next greater number and math.floor to its lower number
print("The product of exponential, the nearest higher number and the nearest lower number of ",p, "is ",u)