def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())



# Multiple Decorator Calls --------------------------------

def changecase(func):
  def myinner():
      return func().upper()
  return myinner

@changecase
def myfunction():
    return "Hello Sally"

@changecase
def otherfunction():
    return "I am speed!"

print(myfunction())
print(otherfunction())