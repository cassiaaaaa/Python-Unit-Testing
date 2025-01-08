import pytest

# Functions
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_palindrome(s):
    return s == s[::-1]

# Tests
@pytest.mark.math
def test_add():
    assert add(3, 2) == 5

# Skipped test
@pytest.mark.skip(reason="This test is temporarily disabled")
@pytest.mark.math
def test_skip_example():
    assert add(1, 1) == 3  # Intentionally incorrect

# Conditional skip using skipif
@pytest.mark.skipif(condition=True, reason="Skipping because the condition is True")
@pytest.mark.math
def test_divide_skipif():
    assert divide(4, 2) == 2

# Expected failure test
@pytest.mark.xfail(reason="Known issue: test case not yet fixed")
@pytest.mark.math
def test_xfail():
    assert divide(1, 0) == 0  # This should raise an exception

# Parameterized test for is_palindrome
@pytest.mark.parametrize("word, expected", [
    ("radar", True),
    ("hello", False),
    ("level", True),
    ("world", False),
])
@pytest.mark.palindrome
def test_is_palindrome(word, expected):
    assert is_palindrome(word) == expected

