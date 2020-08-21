'''
https://py.checkio.org/en/mission/ascending-list/

Determine whether the sequence of elements items is ascending so that its each
element is strictly larger than (and not merely equal to) the element that
precedes it.

Input: Iterable with ints.

Output: Bool.
'''


from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    return True if sorted(items) == items and\
        len(set(items)) == len(items) else False


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) is True
    assert is_ascending([99]) is True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) is False
    assert is_ascending([]) is True
    assert is_ascending([1, 1, 1, 1]) is False
