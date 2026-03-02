# Write to an Existing File -----------------------------------------------------

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

file_name = "demofile2.txt"
with open(file_name,"a") as f: # using ' "a" ' append
    f.write("Hardik Bandhiya....")
    print("Write successfully")

with open(file_name) as f:
    print(f.read())



# Overwrite Existing Content ------------------------------------------------------------------

"""
To overwrite the existing content to the file, use the w parameter:
"""
print("---------------------------------------------------------------------------")

with open("demofile3.txt","w") as f:
    f.write("Woops! I have deleted the content!")

with open("demofile3.txt") as f:
    print(f.read())


f = open("myfile.txt", "x") # "x" - Create - will create a file, returns an error if the file exists
