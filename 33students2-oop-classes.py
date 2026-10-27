class Student():
    def __init__(self, name, house):   
        if not name:
            raise ValueError("Missing Name")
        # if house not in ["Gryffyndor","Hufflepuff","Ravelclaw","Slytherin"]:
        #    raise ValueError("Invalid House")
        self.name = name
        self.house = house
    def __str__(self): 
        return(f"{self.name} in {self.house}") 
    # we are trying to stop programmers circumventing our rules
    # remember functions are just methods inside classess
    # python will automatically use the getter/setter of the same name as the attribute so you have control now
    # Getter
    @property # you have to put this above the function to make a "decorator"
    def house(self):
        return self._house # can't have the same name of the attribute as the 'property'
    # Setter
    @house.setter # this must be above.  why didn't they use house.getter!!
    def house(self,house):
        if house not in ["Gryffyndor","Hufflepuff","Ravelclaw","Slytherin"]:
            raise ValueError("Invalid House")
        # now we don't need the error checking in the init
        self._house = house # can't have the same name of the attribute as the 'property'

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Invalid Name")
        self._name = name
        
def main():
    student = get_student()
   # student.house = "X" # we probably don't want the user to do this!
    # we need to use properties (a type of attribute)
    # need to use decorators
    # we could however update the attribute!
    student._house = "X" # in other languages the attributes can be read only
    # so it's an honouer system - to say 'don't touch this!'
    print(student) 

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)

if __name__ == "__main__":
    main()

# other notes
# int is also a class of course! so we are just making our own data types
# an instance of a class is an object
