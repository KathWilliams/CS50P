import pytest # only need this if you want to reference pytest directly in this code - eg the str 
# raise exception
from modulecalculator import square


# option 1 - is fine but lots of code
"""
# def main():
    if square(2) != 4:
        print("2 squared does not equal 4")
    if square(3) != 9:
        print("3 squared does not equal 9")
    """
# opion 2 - is fine, less code, like the 'assert' but when we run we just get an AssertionError, with no help
# as to where (actually in this version of python we get the line number, but still messy to have a runtime error like this)
"""
def main():
    assert square(2) == 4
    assert square(3) == 9
"""
# option 3 - put try exceptions around, and do more test cases.  
# who wants to write all these lines of code for 1 simple function!
# also, you want to try corner cases eg all positive numbers should work in the same way
# all negative same, perhaps 0?
# this is usually instinct!!
"""
def main():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared does not equal 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared does not equal 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared does not equal 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared does not equal 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared does not equal 0")
    """
# option 4 - download a tool  python have some, but pytest is a downloadable one which is better
# just use the assert and then run pytest instead of python program passing in the program name.
# you will see red or green depending on failure/success and it will show you the result of your test in red
# but it stops at the one that fails! so you don't have all the clues you might need to figure it out
"""
def main():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
"""
# if we passed in "cat" then currently the program would break
# we could get the program to raise an exception and then catch it here but not for now

# if we separate out the asserts then all defs will run and therefore be more helpful in debugging
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
def test_str():
    with pytest.raises(TypeError):
        square("cat")


# really good practice to break your code into testable functions
# functions should only do one thing really