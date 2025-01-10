# import pytest
# from examples.calculator import (
#     add,
#     subtract,
#     multiply,
#     divide
# )

# def test_add():
#     assert add(1,4) == 5
#     assert add(3,10) == 13
#     assert add(20, 12) == 32

# def test_subtract():
#     assert subtract(9,3) == 6
#     assert subtract(39,3) == 36
#     assert subtract(19,2) == 17

# def test_multiply():
#     assert multiply(3,5) == 15
#     assert multiply(9,2) == 18
#     assert multiply(5,1) == 5

# def test_divide():
#     assert divide(27,3) == 9
#     assert divide(90,10) == 9
#     assert divide(49,7) == 7
#     with pytest.raises(ZeroDivisionError):
# 			  divide(10,0)