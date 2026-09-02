numbers = [10, 15, 22, 8, 31, 44]

target = int(input("Enter a number to search: "))

found = False

for number in numbers:
    if number == target:
        found = True

if found:
    print("Element found")
else:
    print("Element not found")