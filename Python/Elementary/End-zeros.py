'''
https://py.checkio.org/en/mission/end-zeros/
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Output: An Int.
'''


def end_zeros1(num: int) -> int:
    total = 0
    for n in str(num)[::-1]:
        if n == '0':
            total += 1
        else:
            break
    return total


# This was a randown answer from checkio.org
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip("0"))


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(100100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
