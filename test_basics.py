def app(a,b):
    return a + b

def test_app():
    assert app(2, 3) == 5

def test_app_negative_numbers():
    assert app(-2,-3) == -5

def test_app_with_zero():
    assert app(0,0) == 0