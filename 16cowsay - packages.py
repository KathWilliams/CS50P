#pypi.org is a list of all external packages available
#cowsay!
# you could download/install manually, or use pip
# pip install cowsay
import cowsay
import sys

if len(sys.argv) == 2:
#    cowsay.cow("hello, "+sys.argv[1])
    cowsay.trex("hello, "+sys.argv[1])
# will print what i pass in, with a cow ascii art!

# command line arguments are all about automation, and speed!  old school but the best
