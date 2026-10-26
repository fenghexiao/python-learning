import pytest

def divide(a,b):
    return a/b

def test_divide_normally():
    assert divide (10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)