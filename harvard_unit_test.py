# Lecture 5: (Unit Test)
#from harvard_calculator import square 
#def main():
#    test_square()
#def test_square():
    #assert square(2) == 4 # 'assert' - allows us to tell the interpreter that something, some assertion, is true.
#    assert square(2) == 4
#    assert square(3) == 9
#    assert square(-2) == 4
#    assert square(-3) == 9
#    assert square(0) == 0
#if __name__ == "__main__":
#    main()

import pytest

from harvard_calculator import square


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

