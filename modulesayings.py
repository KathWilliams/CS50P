def main():
    hello("world")
    goodbye("world")
    
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")
# if we import this module then it will run the main UNLESS we do the following
if __name__ == "__main__":
    main()
# want to understand this a bit more
# every python file has a special variable called __name__
# if run directly - it has __main__
# if imported by another file - it has the module's name
# when you import a module its top level code dpes execute, it's the check on __name++ that stops it running    
# this means you can use a module independently or on its own.  sometimes you write code which is independent
# then later want to share some of its functions.  in other languages you would have to separate out the functions
# and create new code even just to do the first program
# this way means we can experiment and 'prove' the functions work by running it independently 


# module - a single importable unit of python code - the .py file
# package - a way of organising related modules under a common name
# library - a general collecion of reusable functionality
# pip - a tool for installing python distributions (which may provide one or more importable modules or packages)