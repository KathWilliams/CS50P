import re
email = input("what's your email? ").strip()
# usually an email would have an @ and then a '.' in the domain name
"""
if "@" in email and '.' in email: # like an instr - but allows . before @ for example
    print("Valid")
else:
    print("Invalid")

# let's split into username/domain
username, domain = email.split("@")
if username and '.' in domain: # if username has at least one character and not null then will return ok
    print("Valid")
else:
    print("Invalid")

# let's check if the email ends with something
username, domain = email.split("@")
if username and domain.endswith(".edu"): 
    print("Valid")
else:
    print("Invalid")

# we shall start to use the regular expression library
# trivial example first, no better than our first example above
if re.search("@",email):
    print("Valid")
else:
    print("Invalid")

# https://docs.python.org/3/library/re.html
# . means 0 or more of any characters
# * means 0 or more repetitions
if re.search(".*@.*",email): # unfortunately will allow kath@ as * means 0
    print("Valid")
else:
    print("Invalid")
"""
# + means 1 or more repetitions
# if re.search(".+@.+",email): # unfortunately will allow kath@ as * means 0
# if we didn't have + then we could do:
# if re.search("..*@..*",email): # ie at least one character first then another character with 0 or more repetitions
# python is using a finite state machine aka
# non deterministic finite automaton - i remember this from uni!!
# reading from left to right

# if re.search(".+@.+.com",email): #unfortunately the . in .com would be interpreted as any character
# so would allow bom, dom etc
# can we use this \?
# if re.search(".+@.+\.com",email): # this is better but python interprets \. as something else
# we need to treat it as a raw string
# if re.search(r".+@.+\.com",email): # r" means treat any \ as raw data
    # can't use curly brackets

# an example here is a google form - respone validation
# you can also use extra regular expressions in here!
# can even be used in find / replace in vscode
# this would allow 'my email addres is xx@x.com'!
# if re.search(r"^.+@.+\.com$",email): # ^ means match the start of string, $ means end of string
# but would still allow @@@
# [] set of characters
# [^] 'not' set of characters (the 'complement' or opposite)
# if re.search(r"^[^@]+@[^@]+\.com$",email): # removed the '.' with the []
# so we are saying - any character except an @ sign
# the ^ is working differently here when inside []

# what if we want to make it better - ie say we want to include all alpha numeric plus underscore
# if re.search(r"^[A-Za-z0-9_]+@[A-Za-z0-9_]+\.com$",email): 
# if re.search(r"^\w+@\w+\.com$",email): # somebody clever has provided \w to mean the same as this - ie a word
# \W - not a word
# \d - decimal
# \D - not a decimal
# \s - whitespace character.  space or tab
# \S - not whitespace
#if re.search(r"^\w+@\w+\.(com|edu|org)$",email): # ()a list = A|B means A or B

# what if you wanted a word or a space
# if re.search(r"^(\w|\s)+@\w+\.(com|edu|org)$",email):
# what if i wanted to force lower case
# cound put lower() on the end of the input or the email.lower() passing in to the search
# but there are flags in the search to help with this
#.re.IGNORECASE
#.re.MULTILINE
#.re.DOTALL

# you can use f string here
# you could get the user to enter the regular expression (try google forms)
# if re.search(r"^\w+@\w+\.(com|edu|org)$",email, re.IGNORECASE):
# however if i typed a@b.d.com then this would fail, as the \w doesn't include a '.' and this is valid

# (...)
# (?:...) non capturing version (not sure this works?)
# if re.search(r"^\w+@\w+\.\w+\.(com|edu|org)$",email, re.IGNORECASE):
# the above alows a@b.d.com but .... a@b.com would work as it would 'expect' the two dots!
# if i put a parentheses in
# if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|org)$",email, re.IGNORECASE):
# the question mark means whatever is in the () before is optional - there or not
# what if we want a username to have a '.'
# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|org)$",email, re.IGNORECASE):
# remember the brackets relates to the character after that, ie in this case the +
# or we could stop using the \w
if re.search(r"^(A-Za-z0-9_\.)+@(\w+\.)?\w+\.(com|edu|org)$",email, re.IGNORECASE):
# this is still very basic.
# if this is something obvious then find a library as somebody else likely to have done this!
    print("Valid")
else:
    print("Invalid")

# re.match and re.fullmatch help you a bit more
