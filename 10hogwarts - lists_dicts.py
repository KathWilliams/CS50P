"""
# students = ["Hermione","Harry","Ron"] # a list
# print(students) # will print them all in a list, not ideal

print(students[0]) # indexes always start at 0
print(students[1])
print(students[2])

for student in students: # didn't use underscore as i am going to use it later!
        print(student)
# anything that is iterable we can use a for loop
# do not need to initialise variables in python

# what if i want to get a list of numbers of students
# you can do more now as you have each index
for i in range(len(students)): # range accepts a number so couldn't do range(students
# range returns a list so range(3) returns [0,1,2]??
        print(i+1, students[i]) # a bit messy to show 0

# a list is a set of multi values
# a dict is a list of key/values! 
"""
students = ["Hermione","Harry","Ron","Draco"] 
houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]
# dict uses {} to create (but not when getting the data later)
students = {"Hermione": "Gryffindor", # could all be on one line
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Syltherin"
}
"""
print(students["Hermione"]) # Hermione is the key
# so really a list is the same as a dict but with automatic indices of 0, 1 etc
print(students["Ron"])
print(students["Harry"])
print(students["Draco"])
"""
for student in students:
    # print(student) # when doing a print on a dict then it prints the key naturally
    print(student,students[student],sep=", ") 
# if we loop through a dict, student = each name in sequence - python simply does this
# then to get the value we have to go to the students dict again (as the for loop doesn't get the value)

# we can do a list of dictionaries if we have more data to store against the index
# a collection of key/value pairs
students = [ # [ means list, here we are creating a list of dictionaries
    {"name": "Hermione","house": "Gryffindor","patronus": "Otter"},
    {"name": "Harry","house": "Gryffindor","patronus": "Stag"},
    {"name": "Ron","house": "Gryffindor","patronus": "Jack Russell Terrier"},
    {"name": "Draco","house": "Slytherin","patronus": None} # None is a key word in python
]
# how many keys does the dictonary have?  3 (name, house, patronus), and values are the individual values
# so keys are like the columns in Excel
# the name is the first column
# each cell is a value

for student in students: # if we do a for loop on a list we get the first item in the list, which is a dictionary, right?
    print(student["name"],student["house"],student["patronus"],sep=", ")

    
