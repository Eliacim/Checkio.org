'''
https://py.checkio.org/en/mission/sort-array-by-element-frequency/

Sort the given iterable so that its elements end up in the decreasing frequency
order, that is, the number of times they appear in elements. If two elements
have the same frequency, they should end up in the same order as the first
appearance in the iterable.

Input: Iterable

Output: Iterable

Precondition: elements can be ints or strings
'''


from functools import reduce


def frequency_sort(items):
    if len(items) == len(set(items)) or not items:
        return items
    else:
        it = reduce(lambda x, y: x - y, [items.count(it) for it in set(items)])
        rev = True if it != 0 else False
        return sorted(sorted(items, reverse=rev),
                      key=lambda s: items.count(s), reverse=True)


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort([1, 2, 2, 1]))
    print(frequency_sort([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) ==\
        [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) ==\
        ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
