# x = input ("What's x? ")
# y = input ("What's y? ")
# z = int(x) + int(y)
# why isn't this x.int?
# print (z)

# the below is simpler perhaps and more readable for me, but it doesn't show the conversion to int explicitly 
# and it won't handle errors
# a = int(input ("What's a? "))
# b = int(input ("What's b? "))

# print (a + b)

# below might simply be too much for some people, but it is more explicit and shows the conversion to int explicitly
# print (int(input ("What's a? ")) + int(input ("What's b? ")))

# a viscerol reaction - is the code becoming too clever for its own good?! 

a = float(input ("What's a? "))
b = float(input ("What's b? "))

# print (a + b) # will be a float!

# z = round(a + b,2)
# print (round(a + b))
# print (f"{z}") # will be the same as printing z. this is called the f string
# print (f"{z:,}") # will be the same as printing z, but with commas for thousands

# round(number[, ndigits]) -> number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
# [ means something optional, so the brackets are not part of the syntax. If ndigits is negative, it rounds to the left of the decimal point.

# c = round(a / b,2) # we can do this, or more commonly we use the f string approach as below
# print (c)
print (f"{a / b:.2f}") # this is the f string approach, and it is more common. It will round to 2 decimal places, but it will not round to the nearest integer if the number is .5 or greater. It will just truncate the number to 2 decimal places.
# nobody really remembers these : parameters!

