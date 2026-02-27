# Unpacking a Tuple

fruits = ("apple", "banana", "cherry")
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print("--------------------------")
# Using Asterisk* --------------------------------------
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# output : 
# apple
# banana
# ['cherry', 'strawberry', 'raspberry']