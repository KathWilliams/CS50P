# we have so far been doing functional or procedural languages
# start by writing something very procedurally
# 1. write without function
# 2. abstract to functions and add the main() call incase we call it as a module

def main():
    # name = get_name() 
    # house = get_house()
    # name,house = get_student() # one way
    # print(f"{name} from {house}")
    # student = get_student_tuple() # so this is a tuple.  similar to a list but immutable
    #student = get_student_list()
    #if student[0] == "Padma":
    #    student[1] = "Ravenclaw" # this will give a TypeError!!
    # print(f"{student[0]} from {student[1]}")
    # why would you use a tuple.  another way to increase correctness if you want it to be immutable

    # now let's use the dict - this just seems better syntax!  we have all the names/houses into a student pot. 
    # if we have all the names as the keys and not 0, 1 etc then easier when we have more characteristics
    student = get_student_dict()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} in {student['house']}") # use ' and not " in fstring"

def get_name():
    return(input("Name: "))

def get_house():
    return(input("House: "))

def get_student_tuple(): # however so far we can't return a single option. you can't return more than one thing!
    n = input("Name: ")
    h = input("House: ")
    return (n,h) # this is similar to a list (a tuple) but it is immutable (unchangeable)
# we are returning one value which is a tuple
# put brackets around it to make it clearer, but not needed.  you can't actually return two values
# you can have nested tuples, nested lists
# confusingly, tuples created using (), lists [] but both elements accessed by [] - confusing!

def get_student_list(): 
    n = input("Name: ")
    h = input("House: ")
    return [n,h] # now return a list

def get_student_dict():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

def get_student_dict2(): # not created a student dict variable
    name = input("Name: ")
    house = input("House: ")
    return {"name": name,"house": house} # create and return the dictionary on the fly


# so far we are using a very generic structure, even if dict - these are general purpose tools
# wouldn't it be nice to create a datatype called 'Student'!
# this is a class.  like a blueprint for objects/pieces of data


if __name__ == "__main__":
    main()
    