'''
https://py.checkio.org/en/mission/isometric-strings/

Maybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism"? i wish I know this word before.

You need to check that the 2 given strings are isometric. This means that a
character from one string can become a match for characters from another
string.

One character from one string can correspond only to one character from another
string. Two or more characters of one string can correspond to one character of
another string, but not vice versa.

Input: Two arguments. Both strings.

Output: Boolean.

Precondition: both strings are the same size
'''


def isometric_strings(str1: str, str2: str) -> bool:
    res = ""
    for s1 in str1:
        res += str2[str1.find(s1)]
    return True if res == str2 else False


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') is True
    assert isometric_strings('foo', 'bar') is False
    assert isometric_strings('', '') is True
    assert isometric_strings('all', 'all') is True
