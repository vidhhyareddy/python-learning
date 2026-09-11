sentence=input("enetr a sentance:")
print("original sentence:",sentence)
print("Characters:",len(sentence))

def count_vowels(text):
    count=0
    vowels="aeiouAEIOU"
    for character in text:
        if character in vowels:
            count=count+1
    return count

print("Vowels:",count_vowels(sentence))

def count_spaces(text):
    count=0
    space=" "
    for character in text:
        if space==character:
            count=count+1
    return count
print("Spaces:",count_spaces(sentence))

print("Words:",len(sentence.split()))


def reverse_string(text):
    reverse=""
    for character in text:
        reverse=character+reverse
    return reverse
print("Reverse:",reverse_string(sentence))

    


