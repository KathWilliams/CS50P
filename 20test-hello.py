from hellolibraries import hello

# keep tests simple! don't need to have tests for tests!
def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David" # this won't work as the hello function is not returning anything!
    # by changing the way hello function works, to make it more testable, we create better programs
    # the print in the hello function is a 'side effect'
    for name in ["A","B","C"]:
        assert hello(name) == f"hello, {name}"