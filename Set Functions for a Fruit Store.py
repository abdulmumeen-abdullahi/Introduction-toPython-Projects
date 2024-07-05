print("This program uses set built-in function to manage a fruit store","\n")
q=set({"Grape", "Water melon", "Garden Egg", "Apple", "Orange", "Banana", "Pineapple", "Mango", "Pawpaw", "Guava"})
o=set({"Water melon", "Garden Egg", "Apple", "Orange", "Berry"})
print("Fruits in Store A are:", q)
print("Fruits in Store B are:", o,"\n")
print("The common fruits in store A and Store B are: ", q.intersection(o),"\n")
print("The fruits in Store A but not in Store B are: ", q.difference(o),"\n")
print("The uncommon fruits in Store A and Store B are: ", q.symmetric_difference(o),"\n")
print("Is all fruit in Store A also in Store B?"
      "\nAnswer:", q.issubset(o))
print("Is all fruit in Store B also in Store A?"
      "\nAnswer:", o.issuperset(q))
print("Is all fruit in Store B not in Store A?"
      "\nAnswer:", o.isdisjoint(q),"\n")
g=str(q)+str(o)
f=q.copy()
print("Fruits in Store C are:", g,"\n")
print("Fruits in Store D are:", f,"\n")
#-----------------------------------------------Updating the set of values in Store A---------------------------------------
p=input("Enter any new fruit to add to Store A: ")
q.update({p})
print("The new set of fruits we have in Store A is:", q)