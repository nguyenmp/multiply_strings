'''
Given two numeric strings, return their multiple
'''

import pytest

def main(first, second):
    """
    Given two strings of nubmers, returns a string representing it's multiple
    """
    return mult_digit(first, second[0])


def mult_digit(number, digit):
    '''
    Given a number which can be long and a digit which is only one digit,
    returns the multplication of the number with the given digit.

    This is a convenience fucntion, since long form multiplicatino is just
    summing up the multiplciation of smaller digits.

    number (str): a string of at least one digit, e.g. "123"
    digit (str): a string of a single digit, e.g. "1"
    '''

    # This stores the result of a single multiply
    result = []
    carry = 0

    # Walk right to left, multiplying hte digit ot each digit in the number
    # this is how I normally do multiplication in my head...
    for number_digit in reversed(number):
        value = int(digit) * int(number_digit) + carry
        result.insert(0, str(value %10))
        carry = value / 10

    # There might still be a carry from the final multiply, so add that
    if carry:
        result.insert(0, str(carry))

    return ''.join(result)


@pytest.mark.parametrize('first,second', [
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
def test_foo(first, second):
    '''
    Verifies that giving two strings of numbers,
    returns the string of it's multiple
    '''
    assert main(str(first), str(second)) == str(first * second)
