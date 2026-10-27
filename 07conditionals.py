# turn off Settings - inline suggest
def lessthan(a,b):
    return a<b

x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))

# if x<y: x<y is essentially a function and in this case is a Boolean
"""
if lessthan(x,y): # just try a function for fun!
    print("x is less than y")

if x>y:
    print("x is greater than y")

if x == y: # == is conditional 
    print ("x is equal to y")
"""
# the above isn't very efficient - asking questions when we know after qu1 is true that it can't be true
# on the next qu

# let's make this mutually exclusive and make it better code longer term.  my computer doesn't care right now
# but we are looking for good designed/efficient code!
"""
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
# elif x == y: # but surely we don't need this question
else:
    print("x is equal to y") 

if x > y or x < y:
    print("x is not equal to y") # we are reusing code here rather than in the one above
else:
    print("x is equal to y")

# could my code be simpler/better.  could i ask fewer questions/tighten
# will the flowchart be simpler

if x != y:
    print("x is not equal to y") # we are reusing code here rather than in the one above
else:
    print("x is equal to y")
"""
# or simpler perhaps
if x == y:
    print("x is equal to y") # we are reusing code here rather than in the one above
else:
    print("x is not equal to y")