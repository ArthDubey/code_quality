from ..code_quality.function_size import functionSize


def test_function_size_one():
    case = """somevar = 4
                anotherVar = 5
                def function(a, b):
                    some function
                    some very small function
                    which will
                    be considered good;
                function(4, 5)"""
    assert functionSize(case.split('\n')) == [4]
    return True


def test_function_size_two():
    case = """somevar = 4
                anotherVar = 5
                def function(a, b):
                    return good;
                function(4, 5)"""
    assert functionSize(case.split('\n')) == [1]
    return True
