import sys
# https://docs.python.org/3/library/sys.html
# sys.argv
# the list of command line arguments passed to a Python script. 
# argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). 
# If the command was executed using the -c command line option to the interpreter, 
# argv[0] is set to the string '-c'. 
# If no script name was passed to the Python interpreter, argv[0] is the empty string.

# print("hello, my name is",sys.argv[1]) # this is a listpy 
# when we run the code, we pass in argument 1
# py 15name.py Kath
# will print hello, my name is Kath
# 1 is the 2nd index, right?
# so what is the first [0]?
# it's the first argument to the python program! so will be 15name.py

# if you don't pass anything in and try to do something with index 1, then you'll get an error 'IndexError'
# we can use try
"""
try:
    print("hello, my name is",sys.argv[1]) # this is a listpy 
except:
    print("no name passed in!")
# or we can do it another way
if len(sys.argv) < 2:
    print("no name passed in!")
elif len(sys.argv) > 2:
    print("too many arguments passed in")
else:
    print("hello, my name is",sys.argv[1]) 
# if you pass in "Kath Williams" as the second argument then this would give the full name

# there is something better about having your main code not in an 'else' hidden away.
# i'd prefer

# check for errors
if len(sys.argv) < 2:
    print("no name passed in!")
elif len(sys.argv) > 2:
    print("too many arguments passed in")

# print name tag
print("hello, my name is",sys.argv[1]) # but this will error if second argument not passed in

# check for errors
if len(sys.argv) < 2:
    sys.exit("no name passed in!") # this quits the program!
elif len(sys.argv) > 2:
    sys.exit("too many arguments passed in")

# print name tag
print("hello, my name is",sys.argv[1]) # but this will error if second argument not passed in
"""
# now let's assume we will have lots of arguments and we want to print a name tag for each
# check for errors
if len(sys.argv) < 2:
    sys.exit("no name passed in!") # this quits the program!

# print name tag
# if we print all the arguments then we will get the program name too
# here is one way to fix, not preferred though
"""
for arg in sys.argv:
    if arg != sys.argv[0]: 
        print("hello, my name is",arg) 
"""
# this is the better approach
for arg in sys.argv[1:]: # this is called slicing
    print("hello, my name is",arg)
# if we add a number to the end of the slice, that will start counting from the end
# eg for arg in sys.argv[1:-1] would drop off the last argument

