'''from cal import square
def main():
    test_method()

def test_method():
    if square(2) != 4:
        print("2 square is not 4")
    if square(3) != 9:
        print("3 square is not 9")

if __name__ == "__main__":
    main()'''

# Too reduce the size of code "assert" key word is used
'''from cal import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__" :
    main()'''

# Too overcome the AssertionError 
'''
from cal import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 sqaure is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square is not 0")    

if __name__ == "__main__":
    main()'''

# Too reduce the length of code using the "pytest"
'''
from cal import square
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0'''

# Too overcome the bug and to check all conditions
'''
from cal import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0'''

# Adding some other test cases and using pytest library

import pytest

from cal import square

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
        '''try:
        square("cat")
    except TypeError:
        print("str is not support")'''