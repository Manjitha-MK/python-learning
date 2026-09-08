# numbers = (10, 20, 10, 30, 20, 40, 50, 30) output should be 30 40 50

numbers = (10, 20, 10, 30, 20, 40, 50, 30)
unique_numbers = set(numbers)
print("Unique numbers1:", unique_numbers)
sorted_unique_numbers = sorted(unique_numbers)


print("Unique numbers:", sorted_unique_numbers)

for number in sorted_unique_numbers:
    if number > 20:
        print(number)
        