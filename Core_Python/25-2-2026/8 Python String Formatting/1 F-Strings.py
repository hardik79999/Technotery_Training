# F-Strings

txt = f"The price is 49 dollars"
print(txt)



# Placeholders and Modifiers ------------------------------------------


price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # The price is 59.00 dollars


# Perform Operations in F-Strings ----------------------------------------------------


txt = f"The price is {20 * 59} dollars"
print(txt) # The price is 1180 dollars


price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt) # The price is 73.75 dollars



price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt) # It is very Cheap


# Execute Functions in F-Strings -------------------------------------------------------

print("------------------------------------")
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)


# String format() -------------------------------------------
print("----------------------------------------")

price = 49
txt = "The price is {} dollars"
print(txt.format(price)) # The price is 49 dollars 


# Multiple Values ----------------------------------------
print("---------------------------------------------------------")
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price)) # I want 3 pieces of item number 567 for 49.00 dollars.


quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price)) # I want 3 pieces of item number 567 for 49.00 dollars.



age = 23
name = "Hardik"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name)) # His name is Hardik. Hardik is 23 years old.