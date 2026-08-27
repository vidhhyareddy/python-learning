student=input("enter your name:")
print("students name=",student)
a=int(input("enter JAVA marks:"))
b=int(input("enter DS marks:"))
c=int(input("enter LST marks:"))
total=a+b+c
print("total=",total)
average=total/3
print("Average=",average)
if average>=50:
    print("Result=pass")
else:
    print("Result=fail")

