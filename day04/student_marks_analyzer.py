def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def find_min(numbers):
    lowest = numbers[0]

    for number in numbers:
        if number < lowest:
            lowest = number

    return lowest


def pass_fail(numbers):
    passed = 0
    failed = 0

    for number in numbers:
        if number >= 40:
            passed = passed + 1
        else:
            failed = failed + 1

    return passed, failed


marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)


total = calculate_sum(marks)
highest = find_max(marks)
lowest = find_min(marks)
average = total / len(marks)
passed, failed = pass_fail(marks)


print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)
print("Failed:", failed)