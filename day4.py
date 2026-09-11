def greet():
    print("hello")

greet()

def hello(name):
    print("Hello", name)

hello("Manjitha")
hello("Kasun")

def add(a, b):
    print(a + b)

add(10, 20)
add(39, 2)

def multiply(x, y):
    return x * y

results = multiply(10, 2)
new_results = results * 2

print(new_results)

def square(number):
    return number * number

x = square(5)
y= square(3)

print("add square value:",x + y)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(22))
print(is_even(13))

        

