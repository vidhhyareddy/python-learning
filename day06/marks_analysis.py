marks = [80, 65, 90, 80, 70]
total = 0

for mark in marks:
    total = total + mark

print(total)

average=total/len(marks)
print(average)

highest=marks[0]
for high in marks:
 if high>highest:
    highest=high
print(highest)

lowest = marks[0]
for low in marks:
 if low<lowest:
    lowest=low
print(lowest)

analysis={
  "total":total,
  "average":average,
  "highest":highest,
  "lowest":lowest
  
}
print(analysis)

unique_marks= set(marks)
print(unique_marks)

