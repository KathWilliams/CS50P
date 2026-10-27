# regex is a good way to reformat - you could do it manually of course! 
# take a spreadsheet
import re # only needed if want to use regular expressions

name = input("What's your name? ").strip()
"""
if "," in name:
    last, first = name.split(", ")
    # version of .split doesn't allow reg ex
    # what if we want to say the space is optional
    name = f"{first} {last}"
"""

"""
#matches = re.search(r"(.+), (.+)$", name) # you can get back more precise info
#matches = re.search(r"(.+), ?(.+)$", name) # you can get back more precise info make the white space optional
matches = re.search(r"(.+), *(.+)$", name) # the * will strip any extra spaces in the middle
# everything within brackets will be captured and will be returned unless you use (?:...)
# what if they type in Williams, Kath
if matches:
    # last,first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    name = matches.group(2) + " " +matches.group(1)
    # why do we start at 1 and not 0!
    # there is something else in group 0!
print(f"hello, {name}")
"""
# walrus operator - assign and ask ':='
# just tightens up the code
if matches := re.search(r"(.+), *(.+)$", name): # the * will strip any extra spaces in the middle
    name = matches.group(2) + " " +matches.group(1)
print(f"hello, {name}")
