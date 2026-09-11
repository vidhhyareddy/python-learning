def reverse_string(text):
    reverse=""
    for character in text:
        reverse=character+reverse
    return reverse
print(reverse_string("Python"))
