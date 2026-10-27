# so far we are using a very generic structure, even if dict - these are general purpose tools
# wouldn't it be nice to create a datatype called 'Student'!
# this is a class.  like a blueprint for objects/pieces of data
def main():
   student = get_student4()
   # print(f"{student.name} in {student.house}")
   print(student) # if you try to print it, doesn't work as is unless you define a __str__ method defined!
   print(student.charm()) # here i am accessing a method outside the class.  


class Student1: # convention is to use upper case first letter
    ... # ... is a valid placeholder!! this is enough to create a class! this is a definition
    # they are mutable by definition but can be made immutable
    # it's a bit reckless to just leave this blank, but you can


def get_student1():
    student = Student2() # this creates an object - it is an "instance" of the class or instantiation)
    # the data type is 'Student' - we have on the fly created a data type
    # classes have attributes (or properties) or "instance variables" so we use '.' not []
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

class Student2():
    def __init__(self, name, house): # this is a constructor, used for initialising.  a crazy name but avoids clashing with something else
        # why do we have to pass in "self"!! rather than just name and house.  normally we would use return but
        # the convention is to call it 'self' but could be any name.  it is the object itself, it's in the memory
        # it's passing a reference to it, otherwise how would you reference it within the constructor
        self.name = name
        self.house = house
        # instead of adding keys to dictionaries we are adding objects to variables


def get_student2():
    name = input("Name: ")
    house = input("House: ")
    student = Student2(name,house) # a constructor call (instantiate a Student object for me)
    # there is another way using 'new' to do this (constructing) but we can use the init method instead
    return student

def get_student2_better():
    name = input("Name: ")
    house = input("House: ")
     # a constructor call (instantiate a Student object for me)
    # there is another way using 'new' to do this (constructing) but we can use the init method instead
    return Student2(name,house)

# how is class represented in memory - just code!
# the object is just in bytes, and python handles it
# why using classes not dicts? lots more we can do!
# you can error check, etc

class Student3():
    def __init__(self, name, house):   
    # def __init__(self, name, house=None): # the none mean i could not pass in the house and make it optional   
    # if you want to reject if name not entered - 
        if not name:
    # can't just print if not name
    # shouldn't just break out of the program - very extreme!
    # we need to signal an error and stop the object being created at all!
    # we need to create our own errors, like ErrorType = not just catch them!
            raise ValueError("Missing Name")
            # raise KatyError("Missing Name") # can raise your own unique errors!
        if house not in ["Gryffyndor","Hufflepuff","Ravelclaw","Slytherin"]:
            raise ValueError("Invalid House")
# in a dict, stuff is going in regardless!
        self.name = name
        self.house = house
# encapsulate all rules within here rather than in the calling code
    def __str__(self): # defines how you want to display it if somebody just calls the object
        # will know the student it is trying
        # dunder str means double underscore str - simpler way of saying it!
        return(f"{self.name} in {self.house}") 

def get_student3():
    name = input("Name: ")
    house = input("House: ")
    return Student3(name,house)


class Student4():
    def __init__(self, name, house, patronus):   
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffyndor","Hufflepuff","Ravelclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): 
        return(f"{self.name} in {self.house}") 
# the above are two function within a class - known as methods
#we can define our own methods! these are like verbs
    def charm(self): # takes at least one argument
        match self.patronus:
            case "Stag": 
                return "x"
            case "Otter":
                return "y"
            case "Jack Russell Terrier":
                return "z"
            case "_": # 
                return "!" 

def get_student4():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student4(name,house,patronus)


if __name__ == "__main__":
    main()
    