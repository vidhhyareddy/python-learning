def calculate_average(a, b, c):
    return (a + b + c) / 3


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def display_result(name, average, grade):
    print("Student:", name)
    print("Average:", average)
    print("Grade:", grade)


name = input("Enter student name: ")

a = int(input("Enter marks for subject 1: "))
b = int(input("Enter marks for subject 2: "))
c = int(input("Enter marks for subject 3: "))

average = calculate_average(a, b, c)
grade = get_grade(average)

display_result(name, average, grade)