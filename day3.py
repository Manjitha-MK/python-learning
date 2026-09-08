# numbers = (10, 20, 10, 30, 20, 40, 50, 30) output should be 30 40 50

numbers = (10, 20, 10, 30, 20, 40, 50, 30)
unique_numbers = set(numbers)
print("Unique numbers1:", unique_numbers)
sorted_unique_numbers = sorted(unique_numbers)


print("Unique numbers:", sorted_unique_numbers)

for number in sorted_unique_numbers:
    if number > 20:
        print(number)

# 1. List []

fruits = ["apple", "banana", "apple", "orange"]

print(fruits)
print(fruits[1])

fruits.append("mango")

print(fruits)

# list can be change -> fruits[0] = grapes

# 2. Tuple ()

fruits = ("apple", "banana", "apple", "orange")

print(fruits)
print(fruits[1])
print(fruits[-1])

# Tuple is useful when the data should stay fixed. Tuple can't be change -> fruits[0] = grapes XXX

# 3. Set {}

fruits = {"apple", "banana", "apple", "orange", "banana"}

print(fruits)
fruits.add("mango")
fruits.remove("banana")
print(fruits)

# The duplicates are removed. Doesn't work: fruits[0]   # ❌ because set is unordered and doesn't support indexing.