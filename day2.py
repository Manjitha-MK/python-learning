# word = "I am learning python"

# print(word.find("learning"))

# name = "  manjitha kaluarachchi    "

# name = name.strip()
# name = name.title()

# print("Name:",name)
# print("Length of name:", len(name))

# name = input("Enter Your Name: ")
# city = input("Enter Your City: ")

# name = name.strip()
# name = name.title()
# city = city.strip()
# city = city.title()

# print("Name:", name)
# print("City:", city)
# print("Name length:", len(name))
# print("City length:", len(city))

# text = "Python is easy"

# print(text.upper())
# print(text.lower())
# print(text.title())
# print(len(text))
# print(text.count("i"))
# print(text.startswith("Python"))
# print(text.endswith("easy"))

# text = "apple, banana, cherry"

# text1 = text.split()

# print(text1)

# text = "Python-Java-C++-C#"

# print(text.split())

# sent = input("Enter a sentence: ")

# sent= sent.strip()

# print("Uppercase sentence:", sent.upper())
# print("Characters:", len(sent))
# print("Words:", len(sent.split()))
# print("Count of 'PYTHON':", sent.count("Python"))

# Indexing
# Slicing
# .upper()
# .lower()
# .capitalize()
# .title()
# .strip()
# .replace()
# .find()
# .len()
# .count()
# .startswith()
# .endswith()
# .split

# list[index]          → access an item
# list[index] = value  → change an item
# append(value)        → add to the end
# insert(index, value) → add at a position
# remove(value)        → remove by value
# pop(index)           → remove by index


# numbers = [10, 15, 20, 25, 30, 35]

# for number in numbers:
#     if number > 20:
#         print(number)

# numbers = [10, 15, 20, 25, 30, 35, 40]

# for number in numbers:
#     if number % 2 == 0 and number > 20:
#         print(number)

# numbers = [10, 15, 20, 25, 30, 35]

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print(even_numbers)

# numbers = [10, 15, 20, 25, 30, 35]
# list=[]

# for number in numbers:
#     if number > 20:
#         list.append(number)
# print(list)

# numbers = [10, 15, 20, 25, 30, 35, 40]

# odd_numbers = []

# for number in numbers:
#     if number % 2 == 1:
#         odd_numbers.append(number)
# print(odd_numbers)


# numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

# greter_than_20_and_even_numbers = []

# for number in numbers:
#     if number % 2 ==0 and number > 20:
#         greter_than_20_and_even_numbers.append(number)  
# print(greter_than_20_and_even_numbers)

# numbers = [1,4,3,2,6,5,8]
# numbers.sort()
# print("Sorted numbers:", numbers)

# numbers = [1,4,3,2,6,5,8]

# sorted_numbers = sorted(numbers)
# print("Original numbers:", numbers)
# print("Sorted numbers:", sorted_numbers)

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))
# n4 = int(input("Enter fourth number: "))
# n5 = int(input("Enter fifth number: "))

# original = [n1, n2, n3, n4, n5]
# print("Original:", original)
# sorted_numbers = sorted(original)
# print("Sorted:", sorted_numbers)

# for number in original:
#     if sorted_numbers[-1] == number:
#         print("Largest number is:", number)
#     elif sorted_numbers[0] == number:
#         print("Smallest number is:", number)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))
n5 = int(input("Enter fifth number: "))

original_numbers = [n1, n2, n3, n4, n5]
print("Original numbers:", original_numbers)

sorted_numbers = sorted(original_numbers)
print("Sorted numbers:", sorted_numbers)

print("Second largest number: ", sorted_numbers[-2])
