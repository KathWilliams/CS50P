# we can overload an operator eg + is often used as concat
class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def __str__(self):
        return(f"Galleons: {self.galleons}, Sickles: {self.sickles}, Knuts: {self.knuts}")
    # look up special methods like __add_ for overloading
    # you can't create new operators!!
    # but most symbols can be overloaded
    def __add__(self,other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons,sickles,knuts)

potter = Vault(100,50,25)
print(potter) # this won't work unless i define __str__

weasley = Vault(25,50,100)
print(weasley)

# i want to add them all up
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons,sickles,knuts)
# print(total)

# wouldn't it be good to allow us to be able to '+ the whole Vault and it did this
total = potter + weasley # this would work even if the classes are the same, as long as the types are the same
print(total)
