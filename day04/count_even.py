def count_even(numbers):
    
 total=0
 for number in numbers:
    if number%2==0:
        total=total+1
 return total
numbers = [10, 15, 22, 8, 31, 44]
print(count_even(numbers))