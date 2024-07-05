#----------------------------------------String Library----------------------------------------------
y=(input("Enter a word or a sentence: "))
print("Your input is capitalized as: ", y.capitalize(),"\n")
#-------------------------------------------------------------------String Libraries that can be used to confirm input-------------------------
print("This program validate a sign up pin of  6 digit numbers using \'if function\',\' input type\' and \'data length\'")
x=str(input("Enter your pin: "))
if(x.isdigit() and len(x)==6):
    print("You are signed up \nYou will be redirected soon\n")
else:
    print("Incorrect password \nTry again later\n")
#--------------------------------------------------------------------------AFIT's CICT Wi-Fi Confirmation-----------------------------------------------
print("This program confirm the sign in password of AFIT's CICT Wi-Fi of length 2 and in lower case")
i=str(input("User name: "))
o=str(input("Enter your password: "))
if(i,o != int and len(o)==2 and len(i)==2 and i,o.islower()):
    print("You are signed up \nIf nothing happens, refresh the page\n")
else:
    print("Incorrect password \nTry again later\n")
#-------------------------------------------------------------------------To print the last character---------------------------------------
print("This program will return the last character of your input")
p=(input("Enter an eight letters word: "))
print("The last letter of your input is", max(p),"\n")
#----------------------------------------------------------------------To replace an object in our string value----------------------------------
print("This program will replace the python in the value below with java")
a="Welcome to python programming"
print(a)
print("The new value is:", a.replace("python","java"),"\n")
#-----------------------------------------------------------------To turn an input to title style----------------------------------------------------
print("This program will turn your sentence into title style and also split it")
s=input("Enter any sentence: ")
print("The title style of your sentence is:", s.title())
print("Your sentence has been split into:", s.split())