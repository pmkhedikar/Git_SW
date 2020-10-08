def functionTest(n):
    return n**2

def test_success():
    assert functionTest(4)==16

def test_failure():
    assert functionTest(2)==10

def without_test():
    assert functionTest(3)==8
