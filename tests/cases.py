
case_1 = """somevar = 4
            anotherVar = 5
            def function(a, b):
                some function
                some very small function
                which will
                be considered good;
            function(4, 5)"""

case_2 = """somevar = 4
            anotherVar = 5
            def function(a, b):
                return good;
            function(4, 5)"""

case_3 = """myVar = 4
            def iterate(size, n):
                sum = 0
                for i in range(n):
                    sum += size[i]
                return sum
            n = 5
            size = [1, 2]
            for i in range(n):
                sum += size[i]
            iterate([1,2], myVar)
            myVar = 4"""

case_4 = \
    """
# My comment
def arth():
    '''
    This is a helpful comment
    helping everything
    '''
    print("This is a good function)
    # One more helpful statement
 arth()
"""
