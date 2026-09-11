word = input("Enter a word: ")

reverse = ""

for character in word:
    reverse=character+reverse
print(reverse)