x = 23

# z = "my name is hardik " + x
# print(z) # TypeError: can only concatenate str (not "int") to str

#----------------------------------------------------------------------
# F-String

age = 23

all = f"my name is hardik i am {age} year old"
print(all)

#----------------------------------------------------------------------
# Placeholders and Modifiers

marks = 89

txt = f"Total Marks {marks} in 12th"
print(txt) # output : Total Marks 89 in 12th


marks = 89

txt = f"Total Marks {marks:.2f} in 12th"
print(txt) # output : Total Marks 89.00 in 12th