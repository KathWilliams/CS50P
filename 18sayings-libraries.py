import sys
from modulesayings import hello
# the word after 'from' is a python identifier.  not the same as a filename.
# python won't let these begin with a number
# one way to fix this is...
# rename the file to '18...'
# import import.lib
# sayings = import.lib.import_module("18...")
# sayings.hello("kath")

# you cam also import a specific function dynamically.  instead of 'sayings.hello...'
# hello = getattr(module,"hello")
# hello("kath")

# if the library contains a main() then it will run when imported unless... we do something else in the module
# is this a module or a library?

if len(sys.argv) == 2:
    hello(sys.argv[1]) 