print("This program return the name and score of a student in Primary 5 Class using \'__init__\', \'python OOP\', and \'error handling\' \nThis is Ridwanullahi Islamic Group of Schools result confirmation portal for Primary 5 student\n")#This program will run 25 times since we only have 25 students who sat for the last term examination
class student():
    def _init_(self):
        SMS = "Welcome to Primary 5 Class"
        sname = input("Enter the student's Surname: ")
        fname = input("Enter the student's first name: ")
        oname = input("Enter the student's other name: ")
        name=sname + fname + oname
        try:
            score = input("Enter the student's score: ")
        except Exception:(
            print("Input digit numbers not letters nor symbol",
                  "\nRefresh the browser and try again later" ))
        print("\nStudent Name:",sname, fname, oname)
        print("Student Score:",score)
        if int(score)<50:
            print(fname, "is not eligible to be in primary 5\n",fname, "is advice to repeat primary 4")
        else:
            print(SMS,"\n")
    def iterate(self):
        i=0
        while i<25:
            self._init_()
            i+=1
student1=student()
student1.iterate()