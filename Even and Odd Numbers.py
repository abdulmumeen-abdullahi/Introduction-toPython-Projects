print("This program uses the \'range function\' to print even numbers if the start number is an even and odd if otherwise","\n")
l=int(input("Enter any number to start with: "))
k=int(input("Enter any number to stop on: "))
j=2
if  l%2 == 0:
    print("The even numbers between", l, "and", k, "are: ",)
    for x in range(l, k, j):
        print(x)
    print("The odd numbers between", l, "and", k, "are: ")
    for x in range(l+1, k, j):
        print(x)
else:
    print("The odd numbers between", l, "and", k, "are:")
    for x in range(l, k, j):
        print(x)
