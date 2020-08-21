'''
https://py.checkio.org/en/mission/acceptable-password-iii/

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.
Input: A string.

Output: A bool.
'''


def is_acceptable_password(password: str) -> bool:
    number = sum(p.isdigit() for p in password)
    letter = sum(p.isalpha() for p in password)
    return True if number and letter and len(password) > 6 else False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('muchlonger') is False
    assert is_acceptable_password('ashort') is False
    assert is_acceptable_password('muchlonger5') is True
    assert is_acceptable_password('sh5') is False
    assert is_acceptable_password('1234567') is False
