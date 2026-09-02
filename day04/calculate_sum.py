numbers = [10, 15, 22, 8, 31, 44]

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

print(calculate_sum(numbers))