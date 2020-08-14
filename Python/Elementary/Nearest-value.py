'''
https://py.checkio.org/en/mission/nearest-value/

Find the nearest value to the given one.

You are given a list of values as set form and a value for which you need to
find the nearest one.

For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we
need to find the nearest value to the number 9. If we sort this set in the
ascending order, then to the left of number 9 will be number 7 and to the right
- will be number 10. But 10 is closer than 7, which means that the correct
answer is 10.

A few clarifications:

If 2 numbers are at the same distance, you need to choose the smallest one; The
set of numbers is always non-empty, i.e. the size is >=1; The given value can
be in this set, which means that it’s the answer; The set can contain both
positive and negative numbers, but they are always integers; The set isn’t
sorted and consists of unique numbers. Input: Two arguments. A list of values
in the set form. The sought value is an int.

Output: Int.

Example:

nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10 nearest_value({4, 7, 10, 11, 12,
17}, 8) == 7
'''


def nearest_value(values: set, one: int) -> int:
    return min(sorted(values), key=lambda x: abs(x - one))


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    print(nearest_value({5, 10, 8, 12, 89, 100}, 7))
    print(nearest_value({-1, 2, 3}, 0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
