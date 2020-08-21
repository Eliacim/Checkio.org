'''
https://py.checkio.org/en/mission/unix-match-part-1/

Sometimes you find yourself in a situation when, among a huge number of files
on your computer or in a separate folder, you need to find files of a certain
type. For example, images with the extension '.jpg' or documents with the
extension '.txt', or even files that have the word 'butterfly' in their name.
Doing this manually can be time-consuming. 'Matching' or patterns for searching
files by a specific mask are just what you need for these sort of challenges.

This mission will help you understand how this works.
You need to find out if the given unix pattern matches the given filename.

Here is a small table that shows symbols that can be used in patterns.

[seq]   matches any character in seq, for example [123] means any character -
'1', '2' or '3'

[!seq]  matches any character not in seq, for example [!123] means any
character except '1', '2' and '3'

Note that the expression in one pair of square brackets responds only for 1
character. So ('0123', '[!abc]123') == True, but ('00123', '[!abc]123') = False

Input: Two arguments. Both are strings.
Output: Bool.
Precondition: 0 < len(strings) < 100
'''


from re import match


def unix_match(filename: str, pattern: str) -> bool:
    pattern = pattern.replace('.', '\\.').replace('?', '.').replace('*', '.*')
    pattern = pattern.replace('[!', '[^').replace('[]', '[^.]')
    pattern = pattern.replace('[^]', '\\[!\\]')
    return match(pattern, filename) is not None


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') is True
    assert unix_match('1name.txt', '[!abc]name.txt') is True
    assert unix_match('log1.txt', 'log[!0].txt') is True
    assert unix_match('log1.txt', 'log[1234567890].txt') is True
    assert unix_match('log1.txt', 'log[!1].txt') is False
