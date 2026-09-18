data={
    "Name":input("enter name of the student:"),
    "Age":int(input("age of the student:")),
    "Branch":input("enter branch of the student:")
}
marks=[]
for i in range(5):
    mark=int(input("enter marks:"))
    marks.append(mark)
print(marks)

print("Name:", data["Name"])
print("Age:", data["Age"])
print("Branch:", data["Branch"])
def calculate_total(marks):

 total = 0
 for mark in marks:
    total=total+mark
 return total
total = calculate_total(marks)
print(total)

average=total/len(marks)
print(average)

def highest_marks(marks):
 highest = marks[0]
 for high in marks:
  if high>highest:
    highest=high
 return highest
highest=highest_marks(marks)
print(highest)

def lowest_marks(marks):
 lowest = marks[0]
 for low in marks:
  if low<lowest:
    lowest=low
 return lowest
lowest=lowest_marks(marks)
print(lowest)

def pass_fail(marks):
 passed = 0
 failed = 0
 for result in marks:
   if result>=40:
    passed=passed+1

   else:
    failed=failed+1
 return passed , failed
 
passed,failed =pass_fail(marks)

print("passed:",passed)
print("failed:",failed)



unique_marks = set(marks)
print("Unique marks:", unique_marks)

print(marks)
print("Name:", data["Name"])
print("Age:", data["Age"])
print("Branch:", data["Branch"])
print("Marks:", marks)

