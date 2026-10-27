from hellolibraries import hello
# you can add a number of tests into a folder named X and then run "pytests X"
# to do this you need __init__.py in the folder - even if empty

def test_default():
    assert hello() == "hello, world"

def test_arguments():
    assert hello("David") == "hello, David"
