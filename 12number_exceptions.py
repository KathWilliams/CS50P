# print("Hello world) # syntax errors like this must be fixed immediately
# otherwise we need to be prepared defensively
"""
try:
    x = int(input("What is x? "))
    print(f"x is {x}") # f string needed
except ValueError: # this is the error we get if we try to run the code and enter a string
# how do we know what these error names are?
# you can be general but it's bad practice/lazy to do a catch all.  you might miss something
# the documentation is a bit bad what errors can go wrong
    print("x is not an integer")
# try some corner/edge cases
# try 'cat' - this is not a syntax error any more

# best practice is not to do too much in one go, especially if it can produce multiple different errors
# print is unlikely to cause an error, so let's take it out of this error trapping

try:
    x = int(input("What is x? ")) # the int function is failing, so x fails to get evaluated if we pass in 'cat'
except ValueError: 
    print("x is not an integer")
print(f"x is {x}") # f string needed # this gives a new NameError if we enter 'cat'
# the fix could be to separate the int and the input

try:
    x = input("What is x? ")
    x = int(x)
except ValueError: 
    print("x is not an integer")
print(f"x is {x}") # f string needed # this gives a new NameError if we enter 'cat'

# or we could use an else in the original code
try:
    x = int(input("What is x? "))
except ValueError:
    print("x is not an integer")
else: # i only get here if there is no exception
    print(f"x is {x}")

while True: # this allows us to have an infinite loop until the user gives us an integer
    try:
        x = int(input("What is x? "))
    except ValueError:
        print("x is not an integer")
    else: # i only get here if there is no exception
        break   # this feels dirty - 'breaking' - in other languages you would hae a boolean saing when to stop
                # eg while Continue = True
print(f"x is {x}")

# the below is better as we have isolated the getting of the integer into a function.  
# a function should only do one thing really
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    # tab to shift all selected to right.  shift tab to revert
    while True: 
        try:
            x = int(input("What is x? "))
            break # we only get here if x is an integer, but perhaps it is not as 'obvious'?
        except ValueError:
            print("x is not an integer")

    return x

main()

# can we tighten up get_int?

def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    # tab to shift all selected to right.  shift tab to revert
    while True: 
        try:
            x = int(input("What is x? "))
            return x # why waste time breaking and then returning? return is stronger than break!
        except ValueError:
            print("x is not an integer")

main()

# or even get rid of x

def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    # tab to shift all selected to right.  shift tab to revert
    while True: 
        try:
            return int(input("What is x? ")) # are you happy with this, does it makes sense to you? make sure you understand it!
        except ValueError:
            print("x is not an integer")

main()

# what about if we don't want to print anything if an exception, we just want to skip it

def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    # tab to shift all selected to right.  shift tab to revert
    while True: 
        try:
            return int(input("What is x? ")) # are you happy with this, does it makes sense to you? make sure you understand it!
        except ValueError:
            pass
# other languages uses curly brackets, or perhaps begin end
# it is not actually 'tab', it's any number of spaces.  but tab is easier
main()

# other options - is_numeric is an option - checking the conditional is more used in other languages
# this is what i am used to!!
# the pythonic way is a bit more of the mindset of try and error
"""
# if main wants to use the get_int function then it should probably have control over what it calls the variable?

def main():
    x = get_int("What is x? ")
    print(f"x is {x}")
def get_int(prompt):
    # tab to shift all selected to right.  shift tab to revert
    while True: 
        try:
            return int(input(prompt)) # are you happy with this, does it makes sense to you? make sure you understand it!
        except ValueError:
            pass
# other languages uses curly brackets, or perhaps begin end
# it is not actually 'tab', it's any number of spaces.  but tab is easier
main()

# if i want to teach then i need these best practices, and start from worst practice!
# leaving 'raise' for another time!