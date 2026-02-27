
# syntext :::
"""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday") # Thursday
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


# Default Value ---------------------------------------------------


day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _: # default value
    print("Looking forward to the Weekend")



# Combine Values ----------------------------------------------

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday") # Today is a weekday
  case 6 | 7:
    print("I love weekends!")


# If Statements as Guards ------------------------------------------

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")