'''
https://py.checkio.org/en/mission/all-upper/

Check if a given string has all symbols in upper case. If the string is empty
or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean.

Precondition: a-z, A-Z, 1-9 and spaces
'''


def is_all_upper(text: str) -> bool:
    return text.isupper() or not text.strip() or text.isnumeric()


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))
    print(is_all_upper('mixed UPPER and lower'))
    print(is_all_upper(''))
    print(is_all_upper(' '))
    print(is_all_upper('Hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') is True
    assert is_all_upper('all lower') is False
    assert is_all_upper('mixed UPPER and lower') is False
    assert is_all_upper('') is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
