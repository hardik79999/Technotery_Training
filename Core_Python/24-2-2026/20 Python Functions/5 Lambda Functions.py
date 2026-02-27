# Syntax -------------------

# lambda arguments : expression

x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# Why Use Lambda Functions? ----------------------

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(5)

print(mytripler(2)) # lambda Arguments


# Lambda with Built-in Functions ---------------------------

# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


# Using Lambda with filter() -------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


# Using Lambda with sorted() ------------------------

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1]) # The sorted() function can use a lambda as a key for custom sorting:
print(sorted_students) # [('Tobias', 22), ('Emil', 25), ('Linus', 28)]