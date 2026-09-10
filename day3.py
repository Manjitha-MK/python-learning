# # numbers = (10, 20, 10, 30, 20, 40, 50, 30) output should be 30 40 50

# numbers = (10, 20, 10, 30, 20, 40, 50, 30)
# unique_numbers = set(numbers)
# print("Unique numbers1:", unique_numbers)
# sorted_unique_numbers = sorted(unique_numbers)


# print("Unique numbers:", sorted_unique_numbers)

# for number in sorted_unique_numbers:
#     if number > 20:
#         print(number)

# # 1. List []

# fruits = ["apple", "banana", "apple", "orange"]

# print(fruits)
# print(fruits[1])

# fruits.append("mango")

# print(fruits)

# # list can be change -> fruits[0] = grapes

# # 2. Tuple ()

# fruits = ("apple", "banana", "apple", "orange")

# print(fruits)
# print(fruits[1])
# print(fruits[-1])

# # Tuple is useful when the data should stay fixed. Tuple can't be change -> fruits[0] = grapes XXX

# # 3. Set {}

# fruits = {"apple", "banana", "apple", "orange", "banana"}

# print(fruits)
# fruits.add("mango")
# fruits.remove("banana")
# print(fruits)

# # The duplicates are removed. Doesn't work: fruits[0]   # ❌ because set is unordered and doesn't support indexing.

# student = {
#     "name": "Kamal",
#     "age": 22,
#     "course": "AI"
# }

# student["age"] = 23
# student["city"] = "Kandy"

# print(student)
# print(student["age"])
# print(student["city"])

# students = {
#     "Kamal": 75,
#     "Nimal": 45,
#     "Saman": 82
# }

# passed_students = {}

# for name, marks in students.items():
#     if marks > 50:
#         passed_students[name] = marks

# print("Passed students:", passed_students)

# students = {
#     "Kamal": 75,
#     "Nimal": 45,
#     "Saman": 82,
#     "Amal": 68
# }

# passed_students = {}

# for name, marks in students.items():
#     if marks > 70:
#         passed_students[name] = marks

# print(passed_students)


# students = {
#     "Kamal": 75,
#     "Nimal": 45,
#     "Saman": 82,
#     "Amal": 68
# }

# passed_students = {}
# failed_students = {}

# for name, marks in students.items():
#     if marks >= 50:
#         passed_students[name] = marks
#     else:
#         failed_students[name] = marks

# print("Passed students:", passed_students)
# print("Failed students:", failed_students)

# students = {
#     "Kamal": 75,
#     "Nimal": 45,
#     "Saman": 82,
#     "Amal": 68,
#     "Saduni": 35
# }

# print(students)

# passed_students = {}
# failed_students = {}

# for names, marks in students.items():
#     if marks >= 50 :
#         # print("Passed:",names)
#         passed_students[names] = marks
#     else:
#         # print("Failed:",names)
#         failed_students[names] = marks

# print("Passed students:", passed_students)
# print("Failed students:", failed_students)

# student = {
#     "name": "Kamal",
#     "age": 23,
#     "course": "AI"
# }

# student.update({
#     "age": 24,
#     "city": "Kandy"
# })

# student.pop("course")

# print(student)

# students = {
#     "Kamal": 75,
#     "Nimal": 45,
#     "Saman": 82,
#     "Amal": 68
# }

# for name in students:
#     if students[name] >= 70:
#         print(name, students[name])