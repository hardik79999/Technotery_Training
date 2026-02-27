x = 1
y = 2.65
z = 1j # complex

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'complex'>

#------------------------------------------------------------------------
# complex

x = 3+5j
y = 5j
z = -5j
print(type(x)) # <class 'complex'>
print(type(y)) # <class 'complex'>
print(type(z)) # <class 'complex'>

#------------------------------------------------------------------------
# Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))