'''
https://py.checkio.org/en/mission/replace-first/

In a given list the first element should become the last one. An empty list or
list with only one element should stay the same.

example

Input: List.

Output: Iterable.
'''


from typing import Iterable


def replace_first(items: list) -> Iterable:
    return items[1:] + items[0:1]


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))
    print(list(replace_first([])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
