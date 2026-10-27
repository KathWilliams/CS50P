# let's tidy this up to be simple for now
# now let's look at the get_student function.  it's outside the student class
# wouldn't it be better to have everything inside the one class?
# the main can be anywhere you like in the file
# generally the classes would be at the top of the file or in a separate file
class Student():
    def __init__(self, name, house):   
        self.name = name
        self.house = house
    
    def __str__(self): 
        return(f"{self.name} in {self.house}") 
    
    @classmethod # this means we can call this without instantiating the object first.  it would be weird to create the object first
    # this means we can check the data before doing the instantiation
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)
    
def main():
    # student = get_student()
    student = Student.get()
    print(student) 

def get_student(): # not used any more
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)

if __name__ == "__main__":
    main()
