'''
https://py.checkio.org/en/mission/is-even/

Check is the given number is even or not. Your function shoudl return True if
the number is even, andFalse if the number is odd.

Input: Int.

Output: Bool.

Precondition: both given ints should be between -1000 and 1000
'''


def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))
    print(is_even(5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(0) is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
