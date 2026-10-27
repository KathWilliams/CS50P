def main():
    hello()
    name = input ("What's your name? ")
    hello(name)

def hello(to="world"): # everything that is indented is part of the function
    print("hello,",to)
# if i used 'name' in the hello function, it would be a local variable and not the same as the name variable in main
# this is called 'scope' - the scope of a variable is where it can be used

main()