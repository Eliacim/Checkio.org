'''
https://py.checkio.org/en/mission/split-list/

You have to split a given array into two arrays. If it has an odd amount of
elements, then the first array should have more elements. If it has no
elements, then two empty arrays should be returned.

example

Input: Array.

Output: Array or two arrays.
'''


def split_list(items: list) -> list:
    return [[], []] if not items else\
        [items[:len(items)//2], items[len(items)//2:]] if len(items) % 2 == 0\
        else [items[:len(items)//2 + 1], items[len(items)//2 + 1:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))
    print(split_list([1, 2, 3]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
