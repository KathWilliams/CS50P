import random # give me access to the whole library not just .choice
# by doing this, you can also be using the same variables in your code
# from random import choice # this just gets choice into my namespace
# means you can just use choice and have less code.  perhaps also less into the memory?
# https://docs.python.org/3/library/random.html

# do below when you import the library
"""
coin = random.choice(["heads","tails"]) # choice takes a list as an argument []. can you " or ' as long as consistent
# do below if you import just the module?
# coin = choice(["heads","tails"]) # choice takes a list as an argument []. can you " or ' as long as consistent
print(coin)

number = random.randint(1,10)
print(number)
"""
cards = ["jack","queen","king"]
random.shuffle(cards) # this shuffles the list, doesn't return anything
# surely we need to return it into a new list? i didn't think a function could change what you pass in?
# from doc:
#   Shuffle the sequence x in place.
#   To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.

for card in cards:
    print(card)