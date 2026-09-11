sentance=input("enetr a sentance:")
count=0
space=" "
for character in sentance:
    if character==space:
        count=count+1
print(count)