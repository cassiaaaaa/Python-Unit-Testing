import pytest

#Built-in Exceptions
"""----------------Example 1------------------"""

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

"""----------------Example 2-------------------"""
def check_positive(number):
    if number <= 0:
        raise ValueError("The number must be positive.")
        # raise is used here as Python will not automatically raise a ValueError if number <= 0
         
    return "Number is positive."

def test_check_positive():
    # Test case: ValueError is raised if number is non-positive
    with pytest.raises(ValueError):
        check_positive(-1)
    
    # Test case: Function works for positive numbers
    assert check_positive(5) == "Number is positive."


#Custom Exceptions
"""-------------------Create CustomError Class-----------------"""
class CustomError(Exception):
    pass

"""-------------------Create Function-------------------------"""
def authorize_user(username, authorized_users):
    """
    Checks if the username is in the authorized list.
    Raises a CustomError if the user is unauthorized.
    """
    if username not in authorized_users:
        raise CustomError(f"Unauthorized access attempt by: {username}")
    return f"Welcome, {username}!"

"""-------------------Create Unit Test -----------------------"""
def test_authorize_user():
    authorized_users = ["alice", "bob", "charlie"]

    # Test case: Authorized user
    assert authorize_user("alice", authorized_users) == "Welcome, alice!"

    # Test case: Unauthorized user raises CustomError
    with pytest.raises(CustomError, match="Unauthorized access attempt by: eve"):
        authorize_user("eve", authorized_users)

    # Test case: Another authorized user
    assert authorize_user("bob", authorized_users) == "Welcome, bob!"

    