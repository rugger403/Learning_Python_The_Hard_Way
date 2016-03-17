# #This is teaching us more about the possibilities of what/how we can do things
# #with functions


# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#   print "You have %d cheeses!" % cheese_count
#   print "You have %d boxes of crackers!" % boxes_of_crackers
#   print "Man, that's enough for a party!"
#   print "Get a blanket.\n"

# # We can just assign numbers to the arguments
# print "We can just give the function numbers directly:"
# cheese_and_crackers(20,30)


# #We can pass variables through functions
# print "OR, we can use variables from our script:"
# amount_of_cheese = 10
# amount_of_crackers = 50
# cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# #We can just straight math inside the function
# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)

# #We can manipulate the variables inside the functions with numbers
# print "And we can combine the two, variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




#This is a function I created. We have to show 10 different ways of calling a
#function
import decimal
#I used the int() function to turn my raw input strings into integers
puppy_count = int(raw_input("How many puppies were there?"))
kitty_count = int(raw_input("How many kittens were there?"))

def puppies_and_kittens(puppy_count, kitty_count):
  print "Where'd %d puppies come from!?" % puppy_count
  print "There's %d kittens too!?!?" % kitty_count

print "How many puppies were there again? Oh yeah, %d puppies %d kittens" % (kitty_count,puppy_count)
puppies_and_kittens(puppy_count+8, kitty_count + 11)


print "Imagine if they had babies??? There would be %d puppies and %d kittens" % (puppy_count**2, kitty_count**2)

puppies_and_kittens(puppy_count, kitty_count)

print "The ratio of puppies to kittens was %d-to-1." % (float(puppy_count/kitty_count))

print "The ratio of kittens to puppies was %d-to-1" % (float(kitty_count/puppy_count))

print "There are %d more puppies than kittens" % (puppy_count-kitty_count)

print "There are %d less kittens than puppies." % (puppy_count-kitty_count)

print "There are %d more kittens than puppies" % (kitty_count-puppy_count)

print "There are %d less puppies than kittens." % (kitty_count-puppy_count)
