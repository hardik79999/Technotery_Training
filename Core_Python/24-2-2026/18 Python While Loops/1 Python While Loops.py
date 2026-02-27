# The while Loop -----------------------------------

i = 1
while i < 6:
    print(i)
    i += 1


# The break Statement ------------------------------------
print("---------------------------")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1



# The continue Statement -------------------------------------

print("---------------------------")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue # skip the element
    print(i)



# The else Statement -----------------------

print("---------------------------")
i = 1
while i < 6:
    print(i)
    i += 1
else:
  print("i is no longer less than 6")