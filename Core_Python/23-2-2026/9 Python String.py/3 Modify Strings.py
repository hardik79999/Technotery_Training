# Upper Case
a = "hello wOrld"
print(a.upper())

# ------------------------------------------------------------
# Lower Case
a = "Hello WoRld"
print(a.lower())

# ------------------------------------------------------------
# Remove Whitespace

a = "  hello world  "
print(a.strip()) # remove both side space
print(a.rstrip()) # remove right side space
print(a.lstrip()) # remove lift side space

# ------------------------------------------------------------
# Replace String

a = "hello world"
print(a.replace("l","j"))

# ------------------------------------------------------------
# Split String

a = "hello world" # if find space seprate word 
print(a.split()) # output : ['hello', 'world']
