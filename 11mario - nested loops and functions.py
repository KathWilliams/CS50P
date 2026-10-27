"""
print("#")
print("#")
print('#')

for _ in range(3):
    print('#')
    """
def main():
#    print_column(3)
# always abstract the problem first eg create the call to the function
# we are over engineering this a bit deliberately to resolve the next challeng of doing a square!
#    print_row(4)
    print_square(3)

def print_square(size):
# we need to think 2 dimensionally now
    """
    for row in range(size):
        for col in range(size):
            print('x',end="")
        print('\n',end="")
    """
#       print(" ") # could have done this but then surely i would get another blank space?
# but we can now use nested functions too!
    for row in range(size):
        print_row(size)

def print_row(width):
    print('?' * width)

def print_column(height):
#    for _ in range(height):
#        print('#')
# you can change the internal implementation of a function as long as you don't change what it returns, signatues etc
# so let's change it now to do the same work, just in a different way
    print('#\n' * height,end="")

main()