import pytest


def test_m4():
    string = 'abhay'
    assert string.upper() == 'ABHAY', 'Matched'


def test_m5():
    assert False


def test_m6():
    assert 'abhay' == 'Abhay'
