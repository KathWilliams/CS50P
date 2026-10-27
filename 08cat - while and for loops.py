"""
print("meow")
print("meow")
print("meow")

i = 3
while i != 0: # all loops or anything where we are indenting next has a ':'
    print("meow")
    i = i -1

i = 0 # most programmers/computer scientists go from 0 up!
while i < 3:
    print("meow")
    # i = i + 1
    i += 1 # ++ is in C

for i in [0,1,2]: # introducing the concept of a 'list'
    # you can't do for loops like in other languages ie for from 0 to 3
    print("meow")
# but this is very hard coded
# change to call a function!

for _ in range(10):
    print("meow")
# we are not using i for anything other than counting it - a pythonic approach is to label it with an underscore

# print("meow" * 3) # all on the same lines
# print("meow\n" * 3) # but we get an extra new line!

print("meow\n" * 3,end="")
# let's get a positive value
# can't use repeat ... until, so let's use the while True
while True:
    n = int(input("How many meows? "))
    if n < 0:
        continue
    else:
        break

while True:
    n = int(input("How many meows? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
"""
def get_number(): # we don't pass anything in! we just want to return something
    while True:
        n1 = int(input("How many meows? "))
        if n1 > 0:
            return n1 # remember we can't update anything we pass in, so must return it

def meow(n2):
    for _ in range(n2):
        print("meow")

def main():
    number = get_number()
    meow(number)

main()
