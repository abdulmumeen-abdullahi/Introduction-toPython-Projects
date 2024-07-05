print("Python program that performs basic arithmetic operation")
try:
    x=int(input("Enter the first number: "))
except Exception:
    print("Enter digit numbers not letters nor symbol",
                  "\nRefresh the browser and try again later" )
try:
    y=int(input("Enter the second number: "))
except Exception:
    print("Enter digit numbers not letters nor symbol",
                  "\nRefresh the browser and try again later" )
try:
        a = int(input("Enter another number: "))
except Exception:
        print("Enter digit numbers not letters nor symbol",
              "\nRefresh the browser and try again later")
z=int(x)+int(y)
c=int(x)-int(a)
print("The sum/addition of", x, "and", y, "is ", z)
print("The difference/subtraction of ", a,"from",x, "is ", c)
print("The multiplication of ", a,"and",y, "is ", a*y)
print("The division of ", y,"with",x, "is ", y/x)
print(x,"raised with the power of",a, "is ", x**a,
      "\n")
#----------------------------------------------------------------------------------------------------------------------------------
print("The program below performs basic arithmetic operation using PEMDAS (order of operation)")
z=(x-y)**y*a/x+a
print(x, "minus", y,"raised with the power of",a, "divided by",x,"plus",a, "is",z,"\n")
#-----------------------------------------Arithmetic Operation by Passing Arguments-------------------------------------
print("This is an argument function that performs arithmetic operations using passed values only")
t=int(input("Enter any number: "))
u=int(input("Enter any number: "))
def y(t, u):
    sum=t+u
    print("The sum of the two numbers is: ", sum)
    return(sum)
y(t,u)

