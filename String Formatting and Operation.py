import math
print("This program explain the concatenation of strings value")
x='100'
p='500'
print("The concatenation of the string values is ", x+p)
print("and not 600")
#------------------------------Iteration of a string value-----------------------------------------
print("This program will repeat the input value four times")
y=input("Enter any number: ")
print(y*4)
#----------------------------To concatenate any input value---------------------------
q=input("Enter any number: ")
w=input("Enter any number: ")
e=q+w
print("The values input can't be added up but rather be concatenated as ", e)
#------------------------------------------------------------------------------------------------------------------------
print("The program below showcase how to use the special string characters in Python")
print("The \n is use to break a line of code")
print("The \\ is use to insert a backslash in our line of code")
print("The \'is use\' to insert single quotation in our line of code")
print("The \"is use\" to insert double quotation in our line of code")
print("The \t is use to insert an horizontal tab in our line of code")
#----------------------------------------String Indexing and slicing------------------------
print("The program below explain string indexing in Python")
y='Cherished Soul'
print(y[9])#This will print an empty tab
print(y[-4])#This will print s, since it is the 4th character from the right hand
print(y[0])#This will print C, since it is the first character from the left
#--------------------------------------The program below explain string slicing in Python---------------------------------------------------------------------------------
print(y[1:3])#This will print he, since h is the second character from the left and e is the second character before the third
print(y[0:7])#This will print Cherish
print(y[5:11])#This will print Shed s
#--------------------------------------Updating String-----------------------------------------
print("The program below explain how to update string in Python")
u = 'Tinubu'
print(u[:4] + 'ke')
v = 'Tinubi'
print('So' + v[-4:])
del u
print(u) #This will return error since we have deleted varriable u using (del u)
#----------------------------------------------------Forming new sentence from user's input using string formatting -----------------------------------------------
print("This program use the concept of string formatting to form new sentences from user's input\n")
q=str(input("Enter your name: "))
w=str(input("What are you tired of?: "))
print("%s is tired of %s"%(q, w))
#---------------------------------------------------------------------------------------------------------------------------------
e=str(input("Enter your name: "))
r=int(input("How many years of experience do you have? "))
t=str(input("Enter your profession: "))
print("%s has %o years of %s experience"%(e, r, t))
#------------------------------------------------------------------------------------------------
q=str(input("Enter your name: "))
w=str(input("What are you tired of?: "))
print("%s is tired of %s"%(q, w))