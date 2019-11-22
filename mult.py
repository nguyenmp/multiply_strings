'''
Given two numeric strings, return their multiple
'''

import pytest

def main(first, second):
    """
    Given two strings of nubmers, returns a string representing it's multiple
    """
    rows_to_sum = []

    # Multiply the first with each digit of the second,
    # then shift by the magnitude of the second's index
    # Each of these mutiples makes up a row to sum in the end
    for index, second_digit in enumerate(reversed(second)):
        row = mult_digit(first, second_digit)

        # Our offset to the right is the number of trailing zeros to add
        for _ in range(0, index):
            row += '0'

        rows_to_sum.append(row)

    # Add up all the rows to sum, don't forget the carry
    result = []
    carry = 0
    index = 0
    len_of_rows = [len(row) for row in rows_to_sum]
    while index < max(len_of_rows):
        digit = 0
        for row in rows_to_sum:
            if index < len(row):
                digit += int(list(reversed(row))[index])
            else:
                digit += 0
        digit += carry
        result.insert(0, str(digit % 10))
        carry = digit / 10
        index += 1

    if carry:
        result.insert(0, str(carry))

    return ''.join(result)


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
    (9, 12356),
    (10, 10),
    (123456789, 987654321),
    (123456789987654321, 123456789987654321),
])
def test_foo(first, second):
    '''
    Verifies that giving two strings of numbers,
    returns the string of it's multiple
    '''
    assert main(str(first), str(second)) == str(first * second)
