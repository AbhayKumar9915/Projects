import sys
import pytest

"""
-n = Used for running cases parallel (py.test Pytest01.py -n 6) pytest-xdist plugin required 
-v = Increases the verbosity
-s = For printing string values in console
-k and -m are used for grouping of desired test cases to run
-k = Represents the substring to search for in test names (py.test Pytest01.py -n 6 -v -k Great),in m1 and m3
-m = Represents the marker name of the tests to be executed (py.test Pytest01.py -n 6 -v -m Great),in m2 and m5
@pytest.mark.skip/xfail - For skipping test case
@pytest.mark.parametrize - For parametrizing test case
@pytest.mark.skipif - Skipping test case depends on condition
To generate report - pytest .\Pytest01.py --html=report.html
"""


def test_m1_Great_Group():
    assert 9 == 3*3


@pytest.mark.Great
def test_m2():
    name = 'Abhay'
    assert name == 'Abhay'


def test_m3_Great_Group():
    assert True


@pytest.mark.skipif(sys.platform != "win32", reason="does not run on windows")
def test_m4():
    assert False, 'Assert False will always fail'


@pytest.mark.Great
def test_m5():
    sub = 'Python'
    assert 'python' == sub.lower()


def test_m6():
    assert '10' == str(10)


@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_para(num, output):
    assert 11 * num == output, 'Fails when 11*num not equals to output'
