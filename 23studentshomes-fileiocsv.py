"""
students = []
with open("students2.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name,"house": home}
        students.append(student)
for student in sorted(students,key=lambda x: x["name"]):

    print(f"{student['name']} from {student['home']}")
"""
# below is the data in students2.csv
# Harry,Number Four, Privet Drive
# Ron,The Burrow
# Draco,Malfoy Manor
# this is a challenging problem as we have a comma in the actual data within the text file.
# so we get a Value Error
# too many values to unpack (expected 2, got 3)
# we could change the comma to something else less common
# we could put "" around the string (this is common) but they we would have to deal with this in the code
# or... we could think - this is a common problem, is there already a solution in a library.
# standing on the shoulders of giants - yes
# use the csv module. details in the python documentation
# make sure the comma separated home is in quotes

import csv
students = []
with open("students2.csv") as file:
    # for row in csv.reader(file):
        # students.append({"name": row[0],"house": row[1]})
    # or we could make this a bit nicer
    for name, home in csv.reader(file):
        students.append({"name": name,"house": home})

for student in sorted(students,key=lambda x: x["name"]):
    print(f"{student['name']} from {student['house']}")

# you can do read and write in the file at the same time but.... you have to manage where you are at all times
# and jump back eg using seek - a bit like an old cassette!
