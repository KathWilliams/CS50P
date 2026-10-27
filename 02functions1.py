def hello(to="world"): # everything that is indented is part of the function
    print("hello,",to)
hello()
name = input("What's your name? ")
hello(name)
# print(name)

# all functions must be at the top, so it gets confusing if you have code below functions you want to use
# by putting all your 'main' code into a function itself, you can avoid this problem
