"""
with open("students.csv") as file:
    # we now need to split the lines using the comma
    for line in file:
        # row = line.rstrip().split(",") # row is a list not a dictionary
        # print(f"Name is {row[0]}, House is {row[1]}")
        # another way to do this....
        name, house = line.rstrip().split(",")
        print(f"{name} {house}")

usually if you want to change any row in the file, you would read the whole file in close it
then change the list, then open the file back in write mode
there is a way to do it for bigger files all in one

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
"""
    # this 'works' but... is sorting by the whole string.  what if i want to sort by an individual field?
# let#s use dictionaries!
"""
students = []

with open("students.csv") as file:
    for line in file:
        # student = {}
        name, house = line.rstrip().split(",")
        # student["name"] = name # remember " and ' and interchangeable but, you should be consistent
        # student["house"] = house
        # the below is less code
        student = {"name": name,"house": house}
        students.append(student)

def get_name(student): # pass in the dictionary
    return student["name"]

# we have a list of students, and within that we have a dictionary
for student in sorted(students, key=get_name): # you can pass in a function to the key
    # note that when we call the function get_name we are NOT using it traditionally, otherwise we would be
    # expected to pass in a dictionary of type student
    # note that we do not use ().  if we used () it is saying - call the function immediately
    # if we omit the () we are refering to the function itself without executing it.
    # in python, functions are first-class objects. you can pass them around just like integers, lists etc
    # the implementation of 'sorted' is responsible for calling your function with the appropriate argument
    # if we put () within the get_name call then python immediately tries to call it rather htan just referencing it

    # could we do this as lamda, ie not bother creating the function?
    print(get_name)
    get_name2 = get_name
    print(get_name2)
    print(type(get_name))
    print(f"{student['name']} is in {student['house']}") 
    # why have we used ' and not " within the fstring?
    # because we are within an fstring with "" so python would see another " as the end of the fstring
# how do we sort these
# note this is a list of dictionaries
"""
"""
def execute(func,value):
    return func(value)

def square(x):
    x*x

print(execute(square,5)) # we are passing the function around like an object
"""

# so yes we can use lambda (which is an anonymous function)
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name,"house": house}
        students.append(student)
"""
def get_name(student):
    return student["name"]
"""
# for student in sorted(students,key=get_name):
#for student in sorted(students,key=lambda student: student["name"]):
# first parameter to 'lamda' is student, and second is saying get the name from it
# slight better designed as we don't have code only used once
# note the name inside lambda is arbitrary.  could have been the below, as x is simply the parameter name
# as if it had been written inside the separate function
# note that lambda isn't simply shorthand for every possible def
# a lambda can contain only a single expressio whereas a regular function can contain multiple statements
# you can pass multple parameters to lambda function eg lambda x,y,z:
for student in sorted(students,key=lambda x: x["name"]):

    print(f"{student['name']} in {student['house']}")
