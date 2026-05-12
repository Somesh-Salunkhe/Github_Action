
# Imports
from src.math_operations import add, subtract


# Test cases for addition function
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(-1,-2) == -3

# Test case for subtraction function
def test_sub():
    assert subtract(5,3) == 2
    assert subtract(4,3) == 1
    assert subtract(1,-1) == 2
    assert subtract(-1,-1) == 0
    assert subtract(1,1) == 0

