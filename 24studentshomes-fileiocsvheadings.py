import csv
students = []
with open("students3headings.csv") as file:
    for row in csv.DictReader(file): # a Reader returns lists, a DictReader returns dictionaries
    # this will now work if the columns are moved around
    # this is an example of coding defensively! the code is getting better and better
        # students.append({"name": row["name"],"home": row["home"]})
        students.append(row) # you can even simplify this as the "row" is a dictionary

for student in sorted(students,key=lambda x: x["name"]):
    print(f"{student['name']} from {student['home']}")