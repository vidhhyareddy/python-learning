def count_vowels(text):
    count=0
    vowels="aeiou"
    for character in text:
        if character in vowels:
            count=count+1
    return count

print(count_vowels("banana"))
