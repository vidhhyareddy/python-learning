n = int(input("Enter a number: "))

even = ""
odd = ""
total = 0

for i in range(1, n + 1):

    if i % 2 == 0:
        even = even + str(i) + " "
    else:
        odd = odd + str(i) + " "

    total = total + i

print("Numbers:", end=" ")

for i in range(1, n + 1):
    print(i, end=" ")

print()

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Sum:", total)