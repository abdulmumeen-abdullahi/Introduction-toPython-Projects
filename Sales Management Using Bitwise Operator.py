print("This program allows a sales manager to manage stores sales using  \'Bitwise Operator\'")
a=int(input("Enter the value of the Store A sales in $: "))
b=int(input("Enter the value of the Store B sales in $: "))
c=int(input("Enter the value of the Store C sales in $: "))
c+=a
b+=a
print("\nThe sum of  Store C sales and Store A Sales  = Store D sales is: ", c)
print("The sum of  Store B sales and Store A Sales = Store E Sales  is: ", b)
c+=b
print("The sum of  Store D sales and Store E Sales = Store F Sales  is: ", c,"\n")
print("The Value of Store B sales is: ", c and b)
print("The Value of Store C sales is: ", c or b)
print("The Value of Store B sales is: ", not c or b)
#----------------------------------------------------------------------------------------------------------------
print("\nThis program explain Bitwise operation, i.e, working with the conversion of decimal values to binary values")
print("The conversion of the common binary values of Store  A sales and Store E sales is: ", a&b)#& operator convert the given values to binary and return 1 if the last digit of the two values is 1 and 0 if either of them is 0.
print("The conversion of (Store  E sales binary value + Store F sales binary value) when two 0 and 0 + 1 =0, and 1+1 = 1 is: ", b|c)#| operator convert the given values to binary, add them up using the '&' principle, and convert the new binary to decimal.
print("The conversion of (Store  F sales binary value + Store A sales binary value) when two 0 and two 1 = 0, and 0 + 1 =1 is: ", c^a)#^ operator convert the given values to binary, add them up using 'two 0 and two 1 = 0, and 0 + 1 =1' principle, and convert the new binary to decimal.
print("The conversion of (Store  A sales binary value + 1) is: ",~a)
print("The conversion of Store E  sales binary value after shifting the first two bit values from the left to the right is: ", b<<2)#1101 => 001101 => 110100, then shift the 1st 2 zeros from left to right, and convert to decimal
print("The conversion of Store F  sales binary value after shifting three bit values from the right to the  left is: ", c>>3)#11000 => 00011000, then shift the last 3 zeros from right to left, and convert to decimal