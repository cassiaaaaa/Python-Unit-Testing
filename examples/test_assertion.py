#Functions
def multiply(a, b):
    return a * b

# def add(a,b):
#     return a + b

#Unit Test with Assertion
import pytest

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2,5) == 10

# def test_add():
#     assert add(3,4) == 7
#     assert add(9,2) == 11