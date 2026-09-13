# def greet():
#     print("hello")

# greet()

# def hello(name):
#     print("Hello", name)

# hello("Manjitha")
# hello("Kasun")

# def add(a, b):
#     print(a + b)

# add(10, 20)
# add(39, 2)

# def multiply(x, y):
#     return x * y

# results = multiply(10, 2)
# new_results = results * 2

# print(new_results)

# def square(number):
#     return number * number

# x = square(5)
# y= square(3)

# print("add square value:",x + y)

# def is_even(number):
#     # if number % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     return number % 2 == 0

# print(is_even(22))
# print(is_even(13))

# def find_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print(find_max(10, 20))
# print(find_max(29, 30))

# numbers = [10, 25, 7, 42, 18]


# def find_largest(numbers):
#     largest = numbers[0]

#     for number in numbers:
#         if number > largest:
#             largest = number

#     return largest
        
# print(find_largest(numbers))

        
# numbers = [25, 10, 40, 5, 30]

# def find_smalest(numbers):
#     smallest = numbers[0]

#     for number in numbers:
#         if number < smallest:
#             smallest = number

#     return smallest

# print("Smallest number is:", find_smalest(numbers))

# numbers = [10, 15, 20, 25, 30, 35]

# def count_even(numbers):
#     count = 0

#     for number in numbers:
#         if number % 2 == 0:
#             count = count + 1

#     return count
    

# print(count_even(numbers))

# numbers = [10, 15, 20, 25, 30, 35]

# def sum_even_numbers(numbers):
#     sum = 0
#     for number in numbers:
#         if number % 2 == 0:
#             sum += number
#     return sum

# print(sum_even_numbers(numbers))

# numbers = [10, 15, 20, 25, 30, 35,23]

# def count(numbers):
#     count_odd = 0
#     count_even = 0

#     for number in numbers:
#         if number % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1

#     return count_even, count_odd

# even, odd = count(numbers)

# print("Even:", even)
# print("Odd:", odd)


# numbers = [10, 15, 20, 25, 30, 35]

# def get_even_numbers(numbers):
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)

#     return even_numbers     

# print(get_even_numbers(numbers))

# def add(a,c):
#     total = a + c
#     return total 

# results = add(10, 20)

# new_results = results * 2

# print(results)
# print(new_results)

numbers = [10, 15, 20, 25, 30, 35]

def get_odd_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)

    return odd_numbers

result = get_odd_numbers(numbers)

print(result)
