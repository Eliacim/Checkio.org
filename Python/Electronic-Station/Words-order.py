'''
https://py.checkio.org/en/mission/words-order/

You have a text and a list of words. You need to check if the words in a list
appear in the same order as in the given text.

Cases you should expect while solving this challenge:

a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one; two
words in the given list are the same - your function should return False; the
condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces. Input: Two arguments. The
first one is a given text, the second is a list of words.

Output: A bool.
'''


def words_order(text: str, words: list) -> bool:
    r = [text.split().index(w) for w in words if w in text.split()]
    return True if r == sorted(r) and len(set(r)) == len(words) else False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))
    print(words_order('hi world im here', ['here', 'world']))
    print(words_order('hi world im here', ['world', 'im', 'here']))
    print(words_order('hi world im here', ['world', 'world']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) is True
    assert words_order('hi world im here', ['here', 'world']) is False
    assert words_order('hi world im here', ['world']) is True
    assert words_order('hi world im here', ['world', 'here', 'hi']) is False
    assert words_order('hi world im here', ['world', 'im', 'here']) is True
    assert words_order('hi world im here', ['world', 'hi', 'here']) is False
    assert words_order('hi world im here', ['world', 'world']) is False
    assert words_order('hi world im here', ['country', 'world']) is False
    assert words_order('hi world im here', ['wo', 'rld']) is False
    assert words_order('', ['world', 'here']) is False
