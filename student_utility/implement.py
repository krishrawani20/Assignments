import student_utils

marks = []

for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = student_utils.calculate_total(marks)

average = student_utils.calculate_average(marks)

grade = student_utils.calculate_grade(average)

print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)