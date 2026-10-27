name = input("What is your name? ")
"""
if name == "Harry":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == ("Draco"):
    print("Slytherin")
else:
    print("Who?")
"""
# or we can use match
"""
match name:
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
"""
match name: # in other languages you need break statements and all sorts
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")