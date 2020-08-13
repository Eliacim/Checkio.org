'''
https://py.checkio.org/en/mission/acceptable-password-i/

You are at the beginning of a password series. Every mission is based on the
previous one. Going forward the missions will become slightly more complex.

In this mission, you need to create a password verification function.

The verification condition is:

the length should be bigger than 6. Input: A string.

Output: A bool.
'''


def is_acceptable_password(password: str) -> bool:
    return True if len(password) > 6 else False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))
    print(is_acceptable_password('muchlonger'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('muchlonger') is True
    assert is_acceptable_password('ashort') is False
    print("Coding complete? Click 'Check' to earn cool rewards!")
