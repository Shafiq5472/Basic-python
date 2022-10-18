#Calculate a grade of a student from his marks 

mark = int(input("Enter your marks: \n"))

if mark>=90:
    grade= "Ex" 
elif mark>=80:
    grade= "A" 
elif mark>=70:
    grade= "B" 
elif mark>=60:
    grade= "C" 
elif mark>=50:
    grade= "D"
else:
    grade = "f"

print("your grade is",grade)