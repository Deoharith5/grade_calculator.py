# Grade Calculator
# Author: Your Name

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def grade_comment(grade):
    if grade == "A":
        return "Excellent Work!"
    elif grade == "B":
        return "Very Good!"
    elif grade == "C":
        return "Good Effort!"
    elif grade == "D":
        return "Needs Improvement!"
    else:
        return "Must Work Harder!"


results = []

while True:
    try:
        num_students = int(input("Enter number of students: "))
        if num_students > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Enter a number.")


for i in range(num_students):
    print(f"\nStudent {i+1}")

    name = input("Enter student name: ")

    marks = []

    for subject in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter Subject {subject} mark: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input.")

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)
    comment = grade_comment(grade)

    results.append([name, marks, average, grade, comment])


print("\n" + "=" * 80)
print(f"{'Name':<15}{'Average':<15}{'Grade':<10}{'Comment'}")
print("=" * 80)

for student in results:
    print(
        f"{student[0]:<15}"
        f"{student[2]:<15.2f}"
        f"{student[3]:<10}"
        f"{student[4]}"
    )

averages = [student[2] for student in results]

print("\nClass Statistics")
print("-" * 20)
print(f"Class Average: {sum(averages)/len(averages):.2f}")
print(f"Highest Average: {max(averages):.2f}")
print(f"Lowest Average: {min(averages):.2f}")

search = input("\nEnter student name to search: ")

for student in results:
    if student[0].lower() == search.lower():
        print("\nStudent Found")
        print(f"Name: {student[0]}")
        print(f"Marks: {student[1]}")
        print(f"Average: {student[2]:.2f}")
        print(f"Grade: {student[3]}")
        print(f"Comment: {student[4]}")
        break
else:
    print("Student not found.")

with open("student_results.txt", "w") as file:
    for student in results:
        file.write(
            f"{student[0]} | "
            f"Average: {student[2]:.2f} | "
            f"Grade: {student[3]} | "
            f"{student[4]}\n"
        )

print("\nResults saved to student_results.txt")2