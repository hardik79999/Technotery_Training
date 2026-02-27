def countdown(n):
  if n <= 0:
     print("Done!")
  else:
      print(n)
      countdown(n - 1)

countdown(5)


# Base Case and Recursive Case --------------------------

def factorial(n):
  # Base case
  if n == 0 or n == 1:
     return 1
  # Recursive case
  else:
     return n * factorial(n - 1)

print(factorial(5)) # 120 factorial number



def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7)) # 13