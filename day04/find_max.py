def find_max(numbers):
    largest=numbers[0]
    for number in numbers:
        if number>largest:
           largest=number
    return largest
numbers=[10, 15, 22, 8, 31, 44]
print(find_max(numbers))       



