# Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # output : ['banana', 'kiwi', 'mango', 'orange', 'pineapple']


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # output : [23, 50, 65, 82, 100]


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # output : ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) # key function
print(thislist)