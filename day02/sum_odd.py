n=int(input("enter a number:"))
total=0
for i in range(1,n+1):
    if i%2!=0:
        total=total+i
print("sum of odd numbers is:",total)
