from ..code_quality.redundancy_check import redundancy_check
from .cases import *


def test_redundancy_check_one():
    assert redundancy_check(case_1.split('/n')) == 100
    return True


def test_redundancy_check_two():
    assert redundancy_check(case_2.split('/n')) == 100
    return True


def test_redundancy_check_three():
    assert redundancy_check(case_3.split('\n')) == 75
    return True
