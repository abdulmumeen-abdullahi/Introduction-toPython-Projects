print("This program stores the name and scores of student in a CA Test in a dictionary format")
w=str(input("Enter a student name:  "))
q=int(input("Enter the student's score:  "))
r=str(input("Enter a student name:  "))
e=int(input("Enter the student's score:  "))
m=str(input("Enter a student name:  "))
n=int(input("Enter the student's score:  "))
t=dict({w:q})
y=dict({r:e})
b=dict({m:n})
u=w, r,m
i=q, e,n
f=(t,
   y,
   b)
print("The names and scores of the three students are:", f, "respectively")
print("The names of the students you recorded are", u,
      "\nTheir scores are", i, "respectively.")
print("The number of student's score recorded is: ", len(f),"\n")
#--------------------------------------------------------------------Student Register---------------------------------------------------------
d={1:"Ola", 2:"Ayo"}
print("The student's register look like: ", d)
d[3]="Ade"
print("After Ade joined the class, the new register look like: ", d)
d[2]="Supo"
print("After Ayo has been changed to Supo, the updated student's register is: ", d,"\n")
j=input("Enter a student's number to get  his name:  ")
print("The name of the student is: ", d.get(int(j)),"\n")
print("The student's register can be stored in a list as: ", list(d.items()),"\n")
d1={1:"Dada"}
d.update(d1)
print("After Ola has been changed to Dada, the new register is: ", d,"\n")
v=list(d.keys())
print("The student's numbers are:", v,"\n")
v1=list(d.values())
print("The student's names are:", v1)
print(d.pop(2), "has been removed from the register.","\n")
print("The last student on the list", d.popitem(), "has been removed from the register.")
print("The new register is: ", d)