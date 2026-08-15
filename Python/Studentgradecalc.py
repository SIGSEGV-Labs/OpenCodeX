name = input("Enter student name: ")
marks1 = int(input("Enter marks in Subject 1: "))
marks2 = int(input("Enter marks in Subject 2: "))
marks3 = int(input("Enter marks in Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 2

print("Student:", name)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")
