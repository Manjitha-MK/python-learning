# name = "Manjitha"
# age = 25
# height = "180cm"
# is_student = True

# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Is student:", is_student)

# -----------------------------------------------------------------------------

# N1 = int(input("Enter first number: "))
# N2 = int(input("Enter second number: "))

# addition = N1 + N2
# print("Addition:", addition)

# subtraction = N1 - N2
# print("Subtraction:", subtraction)

# multiplication = N1 * N2
# print("Multiplication:", multiplication)

# division = N1 / N2
# print("Division:", division)

# ------------------------------------------------------------------------------

# age = int(input("Enter your age: "))

# if age >=18:
#     print("You can vote")
# else:
#     print("You cannot vote")

# -------------------------------------------------------------------------------

# X = int(input("Enter a number: "))

# if X % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# --------------------------------------------------------------------------------

N1 = int(input("Enter first number: "))
N2 = int(input("Enter second number: "))
N3 = int(input("Enter third number: "))

if N1 >= N2 and N1 >= N3:
    print("The largest number is:", N1)
elif N2 >= N1 and N2 >= N3:
    print("The largest number is:", N2)
else:
    print("The largest number is:", N3)
