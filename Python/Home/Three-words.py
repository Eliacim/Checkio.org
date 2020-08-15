'''
https://py.checkio.org/en/mission/three-words/

Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one
space). The words contains only letters. You should check if the string
contains three words in succession. For example, the string "start 5 one two
three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.

Precondition: The input contains words and/or numbers. There are no mixed words
(letters and digits combined). 0 < len(words) < 100
'''


def checkio(words: str) -> bool:
    res = 0
    for wo in words.split():
        res = res + 1 if wo.isalpha() else 0
        if res == 3:
            return True
    return False


if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))

    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"
