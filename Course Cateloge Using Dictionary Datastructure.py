
#------------------------------------------------------------------------------------------Lustre Academy Course Cateloge----------------------------
a={'Python','Arduino','AI Engineering'}
print("The course titles are: ", a)
value="Course"
s=dict.fromkeys(a,value)
print("The course titles above are stored as: ", s)
k=input("Enter a course title from the courses listed above to confirm if it is still available: ")
print("It is", k in a, "that", k, "is available")