#This example is to show how arguments are to be passed through a function in
#python. Future examples go into how we link scripts to our functions to do more

#Creating a method for two arguments
#This way is pointless however....see next method
def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)


#A much simpler way to pass two arguments through a function
def print_two_again(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
  print "arg1: %r" % arg1

def print_none():
  print "I got nothin'."

#These are calling the functions with the desired arguments
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
