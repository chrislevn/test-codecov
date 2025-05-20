"""
Tests for the calculator module
"""
import pytest
from mypackage.calculator import add, subtract, multiply, divide, square, cube

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 3) == -2
    
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

# Note: We're intentionally not testing square and cube functions
# to demonstrate partial code coverage
