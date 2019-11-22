'''
Given two numeric strings, return their multiple
'''

import pytest

def main(first, second):
    # This stores the result of a single multiply
    row_1 = []
    carry = 0
    for c in reversed(first):
        value = int(second[0]) * int(c) + carry
        row_1.insert(0, str(value %10))
        carry = value / 10

    # There might still be a carry from the final multiply, so add that
    if carry:
        row_1.insert(0, str(carry))

    return ''.join(row_1)

@pytest.mark.parametrize('a,b', [
    (1, 1),
    (1, 0),
    (1, 2),
    (2, 1),
    (2, 0),
    (2, 2),
    (20, 2),
    (13, 2),
    (13, 4),
    (12356, 9),
    # (10, 10),
    # (123456789, 987654321),
    # (123456789987654321, 123456789987654321),
])
def test_foo(a, b):
    assert main(str(a), str(b)) == str(a * b)
