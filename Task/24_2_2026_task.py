"""
Create a Python program to manage basic student information using core data types.

Requirements:

Create variables for:
Student name (string)
Age (integer)
Height (float)
Is enrolled (boolean)

Store subjects in a list (at least 4 subjects).
Store student details in a tuple (name, age, height).

Perform the following:
Print a formatted welcome message using string formatting.
Convert age (integer) into string using casting and print it.
Check if student is older than 18 using comparison operators.
Add a new subject to the list.

Print the total number of subjects using len().
Use:
Comments
At least 3 operators
Boolean condition

"""
main_dict = {

}
status = True
while status:
    print("----------Welcome----------")
    Student = input("Enter a Student Name : ")
    Age = int(input("Enter Student Age : "))
    Height = float(input("Enter Student Height : "))
    choice = input("Do you enrolled : (y) or (n) : ").lower()
    if choice == 'y':
        Is_enrolled = True
    else:
        Is_enrolled = False

    print("--------------------------------")
    All_Student=(Student,Age,Height,Is_enrolled)
    d = {}
    d["name"] = Student
    d["Age"] = Age
    d["Height"] = Height
    d["Is_enrolled"] = Is_enrolled
    main_dict[Student] = d
    print(main_dict)

    str_age = str(Age)
    print("Age type",type(str_age))

    if int(str_age) < 18:
        print("Student is older then (18) ")
    else:
        print("Student not older thenn (18)")

        print("--------------------------------")
    run = input("Do you want Add+ more Student ?? (Yes) or (No):").lower()
    if run == 'no' or run == 'n':
        status = False
        print("Byeee...!!!")
        print("---------------------------")
        print(main_dict)
    else:
        status = True

    

