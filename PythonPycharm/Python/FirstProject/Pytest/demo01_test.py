# Scripts name starts or ends with test, easy to run and manage (Not Necessary)
import pytest


# method name should start with test
def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, 'Value matched'


def test_m2():
    a = 3
    b = 4
    assert a == b


def test_m3():
    assert True
