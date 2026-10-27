import random
class Hat1:

    # ... # a really good convention when starting with nothing
    def __init__(self):
         self.houses= ["Gryffyndor","Hufflepuff","Ravelclaw","Slytherin"] # like a list of constants

    def sort(self, name): # needs self plus one more
        print(name, "is in", random.choice(self.houses))

class Hat2:
    # class variables = these are related to the class not the object!
    # class variables
    # remove the init and create a class variable
    houses = ["Gryffyndor","Hufflepuff","Ravelclaw","Slytherin"]
    @classmethod # must put this above if you want it to be a class
    # this is a decorator, you don't have one for an object method, it is assumed
    def sort(cls, name): # cls is just a made up name.  can't be the word class as this is a reserved name
        print(name, "is in", random.choice(cls.houses))

#hat = Hat1()
# hat.sort("Harry") # we are going to encapsulate this away inside the class

Hat2.sort("Harry")
# we have made this have the ability to have X objects
# what we want is a single version (a singleton)
# you can use a class as a container as stuff related to each other
# let's not instantiate new objects
