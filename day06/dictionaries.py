student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85,
    "city":"Hyderabad"
}
student.pop("city")
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)

numbers = {1, 2, 2,3, 3, 3}
numbers.add(6)
numbers.remove(2)
print(numbers)