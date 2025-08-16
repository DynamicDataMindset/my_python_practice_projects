#**Grade Calculator:** A program that calculates a student's grade based on their score, handling both valid and invalid inputs gracefully.

students_grade = int(input("Please Enter Students Marks: "))

if students_grade >=90 and students_grade <=100:
    print("A")
elif students_grade >=80 and students_grade <=89:
    print("B")
elif students_grade >= 70 and students_grade <=79:
    print("C")
elif students_grade >=60 and students_grade <=69: 
    print("D")
elif students_grade >=0 and students_grade <=59:
    print("F")
else:
    print("Students marks Should be between 0 - 100")