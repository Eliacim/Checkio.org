'''
https://py.checkio.org/mission/acceptable-password-v/solve/

In this mission you need to create a password verification function.

Those are the verification conditions:

- the length should be bigger than 6;
- should contain at least one digit, but it cannot consist of just digits;
- having numbers or containing just numbers does not apply to the password
  longer than 9.
- a string should not contain the word "password" in any case.

Input: A string.

Output: A bool.
'''


def is_acceptable_password(password: str) -> bool:
    number = sum(p.isdigit() for p in password)
    letter = sum(p.isalpha() for p in password)

    return True if ((number and letter and len(password) > 6) or
                    (len(password) > 9)) and\
                   password.lower().count('password') == 0 else False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('short54') is True
    assert is_acceptable_password('muchlonger') is True
    assert is_acceptable_password('ashort') is False
    assert is_acceptable_password('muchlonger5') is True
    assert is_acceptable_password('sh5') is False
    assert is_acceptable_password('1234567') is False
    assert is_acceptable_password('12345678910') is True
    assert is_acceptable_password('password12345') is False
    assert is_acceptable_password('PASSWORD12345') is False
    assert is_acceptable_password('pass1234word') is True
