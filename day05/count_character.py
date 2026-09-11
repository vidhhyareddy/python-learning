word = input("Enter a word: ")
target = input("Enter a character: ")
count=0
for character in word:
    if character==target:
        count=count+1
print(count)