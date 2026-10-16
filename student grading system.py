# student grade management system 
print(" Welcome to the student grading system")
name = input("Enter your name:")
print (" welcome",name)
subjects =[ "OOPS", "Database", "programming", "calculus", "algorithm", "communication skills"]
marks=[]
for subject in subjects:
    mark = int(input(f"Enter your marks for {subject}: "))
    marks.append(mark)
total_marks =sum(marks)
average_marks=round( total_marks/len(subjects) ,2)
print(f"Total marks: {total_marks}")
print(f"average_marks: {average_marks}")
if  average_marks >=90:
    print("Grade A")
elif average_marks >=80:
    print("Grade B")
elif average_marks >=70:
    print("Grade C")
elif average_marks >=60:
    print("Grade D")
else:
    print( "Grade F ")    
