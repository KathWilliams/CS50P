"""
names = [] # an empty list

for _ in range(3):
#    name = input("What's your name? ")
#    names.append(name)
    names.append(input("What's your name? ")) # either way is fine

for name in sorted(names):
    print(f"hello, {name}")
"""
# now we want to save the names to save re-typing!!

# name = input("What's your name? ")
# file = open("names.txt","w") # w means write mode, or will create it if not there. 
# open creates a file handler
# "w" will always recreate though not append
# function/method same
"""
file = open("names.txt","a")
# file.write(name) # will append without newlines
file.write(f"{name}\n")
file.close() # you don't always need to do this everytime
"""
"""
with open("names.txt", "a") as file: # with does an open and close automaticaly.  'file' is just a name
    file.write(f"{name}\n")
"""
# now let's try to read the file instead
with open("names.txt", "r") as file:
    lines = file.readlines()
"""
for line in lines:
    # print("hello, ",line)
    # we get two newlines.  one is from the file (as we added in) and one from the print command
    # we could add an 'end' like below
    # print("hello, ",line,end="")
    # but this is a 'better' way?
    print("hello, ", line.rstrip()) # strip off the end of it and slightly better design eg what if the
    # file doesn't have newlines in it

# we can do this in a similar, easier way using something better in the file handler
with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())
"""
# now let's say we want to sort the names - we can do it directly as we read
"""
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
"""
# or we could make this more compact
"""
names = []

with open("names.txt", "r") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")
"""     
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse = True): # look in the documentation for how functions work eg to reverse the order
    print(f"hello, {name}")
