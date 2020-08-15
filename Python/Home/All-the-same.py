'''
https://py.checkio.org/mission/all-the-same/solve/

In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.

The idea for this mission was found on Python Tricks series by Dan Bader

Precondition: all elements of the input list are hashable
'''


from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return True if len(set(elements)) == 1 or not elements else False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) is True
    assert all_the_same([1, 2, 1]) is False
    assert all_the_same(['a', 'a', 'a']) is True
    assert all_the_same([]) is True
    assert all_the_same([1]) is True
