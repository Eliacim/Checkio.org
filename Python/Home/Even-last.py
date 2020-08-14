'''
https://py.checkio.org/en/mission/even-last/

You are given an array of integers. You should find the sum of the integers
with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the
final element of the array together. Don't forget that the first element has an
index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.

Precondition:
0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
'''


def checkio(array: list) -> int:
    return sum(array[::2]) * array[-1] if array else 0


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests\
           and earn cool rewards!")
