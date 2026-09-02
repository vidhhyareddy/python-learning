def count_digits(number):
    count=0
    while number>0:
        count=count+1
        number=number//10
    return count
print(count_digits(58391))
print(count_digits(42))