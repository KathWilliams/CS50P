# Ask user for their name 
# name = input("What is your name? ")
# = means assignment operator - it is used to assign a value to a variable - in this case, we are assigning the value returned by the input() function to the variable name
name = input("What is your name? ").title().strip()
# there is no right or wrong which way to do this.  i prefer it all on one
name = name.strip() # strip() method is used to remove any leading or trailing whitespace characters from the input string. This is useful because users may accidentally add spaces before or after their name when entering it, and we want to ensure that we are working with a clean string.
# we can't strip in the middle without doing something harder
# there is also lstrip and rstrip  
# name is a str data type - str is short for string - a string is a sequence of characters - can be letters, numbers, symbols, etc. - can be enclosed in single quotes or double quotes - can be empty or contain any number of characters
# str has lots of built-in methods that can be used to manipulate strings - https://docs.python.org/3/library/stdtypes.html#string-methods

# Capitalize the first letter of the name
name = name.capitalize() # capitalize() method is used to capitalize the first letter of the string 

name = name.title() # title() method is used to capitalize the first letter of each word in the string - this is useful for names that may have multiple words, such as "John Smith" or "Mary Jane Watson"

name = name.title().capitalize().strip() # we can chain methods together to perform multiple operations on a string - in this case, we are first capitalizing the first letter of each word in the string, and then capitalizing the first letter of the entire string - this is useful for names that may have multiple words, such as "John Smith" or "Mary Jane Watson"

first, last = name.split(" ") # split() method is used to split a string into a list of substrings based on a specified delimiter - in this case, we are splitting the string on the space character, which will give us a list of the first and last name
print (f"Hello {first}")
# Say hello to the user
# print("Hello, ") # will auto put new line because this is default behavior of print function
# print(name)
# https://docs.python.org/3/builtins/functions.html#print
# print(*objects, sep=' ', end='\n', file=None, flush=False)
#   can use single or double quotes - just be consistent with your choice
#   positional paramaters - can be used in any order but must be in the order they are defined in the function definition
#   named paramaters - must be used in the order they are defined in the function definition
#   *objects - can take any number of objects and print them all in one line - can even be 0 arguments!
# print("Hello, ",end="") # will change default behavior of print function to not put new line at the end of the print statement
# print(name)
# print("Hello, " + name)
# print("Hello," , name)
# print("Hello, ", input("What is your name? "),", how are you?") # so this is like concatenating the input with the string and print
# print("Hello, ", input("What is your name? "),", how are you?", sep="") # the sep parameter is used to specify what character(s) should be used to separate the objects being printed - in this case, we are using an empty string so there will be no space between the objects being printed
"""
multi comments
"""
# print ("hello, "friend"") # won't be allowed
# print ('hello, "friend"') # will be allowed
# print ("hello, \"friend\"") # will be allowed - the backslash is used to escape the double quotes so that they are treated as part of the string and not as the end of the string
# f-string
print (f"Hello {name}") # f-strings are a way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.

