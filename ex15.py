
#takes the arguments into the script
from sys import argv

#declaring this file a script and assigning a variable to the input
script, filename = argv

#assigning a file object
txt = open(filename)

#takes the name of the file from the input
print "Here's your file %r:" % filename

#prints the file object
print txt.read()

#requests confirmation of the filename
print "Type the filename again:"

#assigns the input to a variable
file_again = raw_input("> ")

#creates a file object called txt_again
txt_again = open(file_again)

#prints out the try_again file object in a readable format
print txt_again.read()
