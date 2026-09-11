def count_spaces(text):
    count=0
    space=" "
    for character in text:
        if space==character:
            count=count+1
    return count
print(count_spaces("Python is very useful"))
    
