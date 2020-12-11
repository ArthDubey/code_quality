from ..code_quality.function_size import functionSize
from .cases import *


def test_function_size_one():
    assert functionSize(case_1.split('\n')) == [4]
    return True


def test_function_size_two():
    assert functionSize(case_2.split('\n')) == [1]
    return True


def test_function_size_three():
    assert functionSize(case_3.split('\n')) == [4]
    return True
