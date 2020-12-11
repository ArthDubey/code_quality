from ..code_quality.comments_disitribution import commentsDistributionScore
from .cases import *


def test_comments_one():
    assert commentsDistributionScore(case_1.split('\n')) == 0
    return True


def test_comments_two():
    assert commentsDistributionScore(case_2.split('\n')) == 0
    return True


def test_comments_three():
    assert commentsDistributionScore(case_3.split('\n')) == 0
    return True


def test_comments_four():
    assert commentsDistributionScore(case_4.split('\n')) == 100
    return True
