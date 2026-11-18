# name = "Manjitha"
# age = 26
# degree = "BSc in Computer Science & AI"

# print("Name :", name)
# print("Age :", age)
# print("Degree :", degree)

# print("------------------------------")

# number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive")
# elif number < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# print("------------------------------")

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# print("------------------------------")

# total = 0
# number = 1

# while number <= 100:
#     total += number
#     number += 1
# print("The sum of numbers from 1 to 100 is:", total)

# tot = 0
# for number in range(1, 101):
#     tot += number
# print("The sum of numbers from 1 to 100 is:", tot)

# print("------------------------------")

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(4))  # True
# print(is_even(7))  # False

# print("------------------------------")


# def find_largest(n1, n2, n3):
#     if n1 >= n2 and n1 >= n3:
#         return n1
#     elif n2 >= n1 and n2 >= n3:
#         return n2
#     else:
#         return n3

# print("The largest number is:", find_largest(10, 20, 15))  # 20

# marks = [85, 92, 78, 96, 88]
# marks.append(90) # Adding a new mark to the list
# marks.remove(78) # Removing a mark from the list
# marks.sort() # Sorting the marks in ascending order
# marks.reverse() # Reversing the order of the marks
# print(marks.index(88)) # Finding the index of a specific mark
# marks[2] = 95 # Updating a mark at a specific index
# print("Marks:", marks)

# total = 0
# for mark in marks:
#     total += mark
# print("Total marks:", total)

# print("------------------------------")

# marks = [85, 92, 78, 96, 88]

# def find_largest(marks):
#     largest = marks[0]

#     for mark in marks:
#         if mark > largest:
#             largest = mark
#     return largest

# print("The largest mark is:", find_largest(marks))

# def find_smallest(marks):
#     smallest = marks[0]

#     for mark in marks:
#         if mark < smallest:
#             smallest = mark
#     return smallest

# print("The smallest mark is:", find_smallest(marks))



# def count(marks):
#     count_even = 0
#     count_odd = 0
#     for mark in marks:
#         if mark % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#     return count_even, count_odd

# even, odd = count(marks)
# print("The number of even marks is:", even)
# print("The number of odd marks is:", odd)

# print("------------------------------")

# fruits = ["apple", "banana", "orange","apple", "kiwi", "mango"]
# print("Fruits:", fruits)
# print(set(fruits))

# print("------------------------------")

# students = {
#     "Kamal": 75,
#     "Nimal": 45,
#     "Saman": 82,
#     "Amal": 68,
#     "Saduni": 35
# }

# print("Students:", students["Amal"])
# highest_mark = 0
# for names, marks in students.items():
#     if marks > highest_mark:
#         highest_mark = marks
#         top_student = names

# print("The student with the highest marks is:", top_student, highest_mark)



# print("------------------------------")

# marks = [10, 15, 20, 25, 30, 35]

# def get_marks(marks):
#     even_marks = []
#     odd_marks = []

#     for mark in marks:
#         if mark % 2 == 0:
#             even_marks.append(mark)
#         else:
#             odd_marks.append(mark)

#     return odd_marks, even_marks

# odd, even = get_marks(marks)

# print("odd marks:", odd)
# print("even numbers:", even)

from turtle import st


print("------------------------------")

students = {
    "Kamal": 75,
    "Nimal": 45,
    "Saman": 82,
    "Amal": 68,
    "Saduni": 35
}

for names, marks in students.items():
    if marks >= 75:
        print(names, "A pass","marks:", marks)
    elif marks > 60:
        print(names, "B pass", "marks:", marks)
    elif marks > 50:
        print(names, "C pass", "marks:", marks)
    elif marks > 35:
        print(names, "S pass", "marks:", marks)
    else:
        print(names, "Fail", "marks:", marks)

highest_marks = 0
for names, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = names

print("Top student is:",top_student, "Mark is:",highest_marks)

def cal_avg(students):
    total = 0
    avg = 0
    for marks in students.values():
        total += marks
        avg = total/len(students)

    return total, avg
total,avg  = cal_avg(students)

print("Toatal:",total)
print("Average:",avg)

lowest_mark = 0
for name,marks in students.items():
    if marks < lowest_mark:
        lowest_mark = marks
        n = name

print("The lowest score get:",name)

def count_student_greater_than_50(students):
    count = 0
    for marks in students.values():
        if marks > 50:
            count += 1
    return count

count = count_student_greater_than_50(students)
print("Greater than 50 score:",count)

def students_who_scored_above_the_class_average(students):
    total = 0

    for marks in students.values():
        total += marks
        avg = total/len(students)

    above_average_students = {}

    for names, marks in students.items():

        if avg < marks:
            above_average_students[names] = marks

    return avg , above_average_students

avg , student_list = students_who_scored_above_the_class_average(students)


print("Average score:", avg)
print("student_of_greater_than_average_score", student_list)