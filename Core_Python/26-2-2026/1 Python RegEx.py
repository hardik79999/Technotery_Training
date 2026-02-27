import re


nameage = '''
            Hardik is 23 and Ravi is 20
            Jay is 22 and Subham is 24

'''


age = re.findall(r'\d{1,3}',nameage) # '\d' use for digit like a (0-9) # {1,3} only 2 digit
age2 = list(map(int,(re.findall(r'\d{1,3}' , nameage)))) # [23, 20, 22, 24]
# map(function, iterable,..)
print(age)
print(age2)

name = re.findall(r'[A-Z][a-z]*',nameage)

print(name)

d = {}

# for k in name:
#     for v in age:
#         d[k]=v

# print(d)
x = 0
for k in name:
    d[k] = age[x]
    x += 1

print(d)

txt = """
        Mary Fortune (1832–1911) was an Australian writer who was one of the earliest female authors of 
        detective fiction. Born in Ireland, she lived in Canada before moving to the Australian goldfields 
        in 1855. She began writing for local newspapers soon after her arrival, and was a prolific pseudonymous 
        contributor to The Australian Journal for more than four decades. Her writing primarily consisted of short 
        crime stories – including her best-known work, the 500-story series The Detective's Album (pictured) – but also 
        included serial novels, journalism, poetry, and a memoir. She also wrote romances, Gothic fiction, and ghost stories. 
        Her writing drew on her experiences in the goldfields and in Melbourne's rapidly urbanising environment; she often 
        criticised colonial society and its treatment of women. Despite her popularity as a writer, Fortune experienced unstable 
        housing and alcoholism, and died in poverty. Her identity, obscured by pseudonyms, was not rediscovered until the 1950s
"""

for i in txt.split():
    if re.search('also',i):
        print(i)


for i in re.finditer('also',txt):
    result = i.span() #  (start_index, end_index)
    print(i.group(),result) # also (558, 562)    # group() return matched text  

print(txt[558:563]) # also
print(txt[1067:1073]) # 1950s


print("------------------------------------------------------------------")


st = 'sat,hat,mat,cat,bat,pat'

for i in re.finditer('[sc]at',st):
    r = i.span()
    print(r)

result = re.findall('[sch]at',st)
print(result)

for i in result:
    print(i)

print("---------------------------------------")
s = 'sat,hat,mat,cat,bat,pat'
some = re.findall('[^c-h-p]at',s) # using this '^' not include in result
for i in some:
    print(i)


print("------------------------------------------")

food = 'hat rat mat pat'

regex = re.compile('[r]at') # using 'Compile' replce items
food = regex.sub('food',food)
print(food)
print("-------------------------------------------")
d = "hello all \\ all"

print(d) # hello all \
print(re.search(r'\\ all',d)) #<re.Match object; span=(10, 15), match='\\ all'>

print("----------------------------------")

ranst = '123456789h'

print("Matches : " , re.findall('\d',ranst)) # Matches :  ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Matches : " , re.findall('\D',ranst)) # use Capitale '\D' find non digit result

print("Matches : " , len(re.findall('\d',ranst))) # use Capitale '\D' find non digit result

print("Matches : " , len(re.findall('\d{5}',ranst))) # use '{}' find number

n = '1234 1234 12346 1234567'
print("Matches : " , len(re.findall('\d{5,7}',n))) # use '{5,7}' find  5 to 7 all number


phone = '4351-436-2445'
# [a-zA-Z0-9_]
#\W [^a-zA-Z0-9_]
if re.search("\w{3}-\w{3}-\w{4}",phone):
    print("valide Phone nummber")
if re.search("\d{3}-\d{3}-\d{4}",phone): # thie is perfect find the phone number 
    print("valide Phone nummber")



print("---------------------------------------------")

email = "hardik@gmail.com hjg@vom fs.com ufhnfd$shf@ngiu@.com"

print("matches Email :" , re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',email))