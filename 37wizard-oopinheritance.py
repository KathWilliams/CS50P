class Student_old:
    def __init__(self, name, house):
        if not name: 
            raise ValueError("Missing Name")        
        self.name = name
        self.house = house
        ...

class Professor_old:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

# we are duplicating some shared code.  redundancy! as soon as we are copying/pasting code - stop!
# they are both wizards!

class Wizard:
    def __init(self,name):
        if not name:            
            raise ValueError("Missing Name")        
        self.name = name

# now we can remove some of the duplication

class Student(Wizard): # putting this in brackets means use it to inherit from
    def __init__(self, name, house):
        super().__init__(name) # super is a way of accessing the parent class.  can be nested.  
        # if Person is the higher level of Wizard then super would just contain all the stuff from both
        self.house = house
        ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) # this can be nested
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry","Gryffindor")
professor = Professor("Severus","Defence Against The Dark Arts")

# exceptions are good examples of hierarchy/inheritance
# eg BaseException:Exception:ArithmeticError:ZeroDivisionError
# look in Exceptions documentation
# you could handle the BaseException instead

