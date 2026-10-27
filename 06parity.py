# is my number even or odd
"""
x = int(input("What is your number? "))
if x%2 == 0:
    print("even")
else:
    print("odd")
"""
# assuming a function already exists is a good programming concept
def is_even(number): # you can't change the value you pass in.  you could in other languages
#     return number % 2 == 0 # i love this way, why isn't it popular? it is!!  i was just a bit ahead
# i did THE MOST ELEGANT WAY NATURALLY
    return True if number % 2 == 0 else False # apparently this is 'pythonic' - ie the way python does it!
# if you had a function that returned a string, you could also use other string commands on your function
"""
could have done this instead but quite long winded
    if x % 2 == 0:
            return True
    else:
        return False
"""
def main():
    x = int(input("What is your number? "))
    if is_even(x):
        print("even")
    else:
        print("odd")  

main()