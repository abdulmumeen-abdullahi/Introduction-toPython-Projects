print("This program concatenate the for loop, tuple indexing, built in functions of tuple, and pre-defined methods of tuple to create an item list in a local fruit store")
q=('Grape', 'Water melon', "Garden Egg", "Apple", "Orange", "Banana", "Pineapple", "Berry", "Mango", "Pawpaw", "Guava")
print("Our item list is",q,'\n')
t=(input("Enter the fruit you want to buy to confirm if it is available, \n\'True\' means it available and \'False\' means it is not: "))
print("It is",t in q,"that",t,"is available\n")#This use the membership function of tuple
#-----------------------------------------------------------e is the sequence of orders we received today----------------------------------------
e=("Grape", 'Water melon', "Garden Egg", "Garden Egg", "Apple", "Pineapple", "Apple", "Orange", "Banana", "Mango", "Pawpaw", "Guava", 'Water melon', "Garden Egg", "Apple", "Pineapple", "Berry", "Mango", "Pawpaw", "Guava")
print("The number of Apple sold today is",e.count('Apple'),"\n") #Use the count()
#------------------------------------------------------------------------------------------------------------
y=input("Did you know the item number of the fruit you want to buy? \nIf no, enter the fruit here: ")
print("The item number of",y, "is", q.index(y),"\n")  #index()
#----------------------------------------------+() is used to concatenate strawberry to q without rewritting q--------------------
v=tuple(list['Strawberry'])
u=q+v
print("Due to the request of our customers, our new item list is: ", list(enumerate(u)),"\n")
#-------------------------------------------------------------------for loop in tuple-------------------------------
for w in ("Orange", "Garden Egg"):
    print("Garden Egg is sold out")
#-----------------------------------------------To avoid misinterpretation of the subsequent output, orange was removed from the output of sold out
u=list(u)
u.remove(w) #We can only remove one value from our tuple. So, Orange won't be removed
print("Our new item list is: ", list(enumerate(u)),"\n")
#----------------------------------------------------------all() is used to confirm if all our stored value is iterable
print(all(u), ": It return true because all",list(enumerate(u)),"are iterable")
v=('Grape', 'Water melon', "Garden Egg", "Apple", "Orange", "Banana", "Pineapple", "Berry", "Mango", "Pawpaw", "Guava", 'false', 0)
print(all(v), ": It return false because 0 in",v, "is not iterable in\n")
h=(1,2,3,8,9,0,3,45,6,7)
print(all(h), ": It return false because 0 in",h,"is not iterable\n")
#-----------------------------------------------any() is used to confirm if any of our stored value is iterable
print(any(v), ": It return true because one (or more) of the values in",v,"is iterable\n")
#len() is used to know the numbers of our stored value
print("The number of available fruit is:", len(u))
#sorted() is use to arrange our stored value in ascending order and sorted(q, reverse=True) in descending order.
print("Available fruits can be arrange alphabetically as:", sorted(q),
      "\nand in descending order as:", sorted(q, reverse=True),"\n")
#-------------------------------------------------------------------------Adding some fruits to our item list-------------------------------------------------------------
y=list(q).extend(["Apricots", "Butternut squash", "Cherry"])#.extend() is used to add some fruits to our item list
i=list(q).sort()#To arrange our items in an alphabetically order
u=list(q).remove("Garden Egg")
e=enumerate(q)
print("The available fruits are", list(e),"\n")
#---------------------------------------------------------------------------------------------------------
class list():
    w=int(input("Enter the item number of the fruit you want to buy: "))
    if(w==0, 5, 8):
        print("The price of ", q[w], "is $10")
    elif(w==1, 3, 7):
        print("The price of ", q[w], "is $13")
    elif(w==2, 4, 6):
        print("The price of ", q[w], "is $15")
    else:
        print("The price of ", q[w], "is $20")
r=input("Which fruit do you want us to add to our list?\nReply: ")
print("Thanks for your feedback. Next time you come here, our fruit list will include", r)