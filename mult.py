'''
Given two numeric strings, return their multiple
'''

import pytest

def main(first, second):
    return str(int(first) * int(second))

@pytest.mark.parametrize('a,b', [
    (1, 1),
    # (1, 0),
    # (1, 2),
    # (2, 1),
    # (2, 0),
    # (2, 2),
    # (10, 10),
    # (123456789, 987654321),
    # (123456789987654321, 123456789987654321),
])
def test_foo(a, b):
    assert main(str(a), str(b)) == str(a * b)
