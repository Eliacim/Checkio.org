'''
https://py.checkio.org/en/mission/caesar-cipher-encryptor/

Caesar Cipher (encryptor)
Elementary+

This mission is the part of the set. Another one - Caesar cipher decriptor.

Your mission is to encrypt a secret message (text only, without special chars
like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is
replaced by another that stands at a fixed distance. For example ("a b c", 3)
== "d e f"


Input: A secret message as a string (lowercase letters only and white spaces)
Output: The same string, but encrypted

Example:

to_encrypt("a b c", 3) == "d e f"
to_encrypt("a b c", -3) == "x y z"
to_encrypt("simple text", 16) == "iycfbu junj"
to_encrypt("important text", 10) == "swzybdkxd dohd"
to_encrypt("state secret", -13) == "fgngr frperg"

How it is used: For cryptography and to save important information.

Precondition:
0 < len(text) < 50
-26 < delta < 26
'''


def to_encrypt(text, delta):
    newtext = ''
    for t in text:
        case = 97 if t.islower() else 65
        newtext += chr((ord(t) + delta - case) % 26 + case)\
            if t.isalpha() else t
    return newtext


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))
    print(to_encrypt("simple text", 16))

    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
