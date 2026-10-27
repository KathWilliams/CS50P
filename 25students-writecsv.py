import csv

name = input("What's your name? ")
house = input("What's your house? ")

# when using python csv module always open CSV files withy newline="" for both reading and writing
# otherwise in Windows certainly you will get an extra newline
# doesn't happen in the course as he is using Linux/macOS
# in windows it might work differently!
"""
with open("students4append.csv", "a", newline="") as file:
    writer = csv.writer(file)
    # it's on us to to send in a list of fields in right order
    writer.writerow([name,house])
"""
# can we write a dictionary not a list?
with open("students4append.csv", "a", newline="") as file:
    writer = csv.Dictwriter(file, fieldnames=["name","home"])
    # in theory we could send in these in different order now as it is a dict so 'more intelligent'!
    writer.writerow({"name":name,"house": house})