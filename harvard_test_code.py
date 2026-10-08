# Lecture 5: (Testing String)
from harvard_testing_string import hello

def test_hello():
    assert hello("David") == "hello, David" # 'assert' - “check that this is true.”
    assert hello() == "hello, world"