word=input("enter a word:")
count=0
vowels="aeiou"
for character in word:
    if character in vowels:
        count=count+1
print(count)
    
