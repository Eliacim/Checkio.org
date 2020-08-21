'''
https://py.checkio.org/mission/wrong-family/


You have a list of family ties between father and son. Each element on this
list has two elements. The first is the father's name, the second is the son's
name. All names in the family are unique. Check if the family tree is correct.
There are no strangers in the family tree. All connections in the family are
natural.

Input: list of lists. Each element has two strings. The list has at least one
element

Output: bool. Is the family tree correct.

Precondition: 1 <= len(tree) < 100
'''


from collections import defaultdict


def is_family(tree):
    fam = defaultdict(set)
    for father, son in tree:
        if (
            (father in (son, fam[son])) or
            (son in fam[father]) or
            (fam[father] & fam[son])
           ):
            return False
        fam[son] = fam[son] | {father} | fam[father]
    return len([f for f in fam if not fam[f]]) == 1


if __name__ == "__main__":

    print(is_family([['Logan', 'Mike'], ['Logan', 'Jack']]))

    assert is_family([['Logan', 'Mike']]) is True,\
        'One father, one son'

    assert is_family([['Logan', 'Mike'], ['Logan', 'Jack']]) is True,\
        'Two sons'

    assert is_family([['Logan', 'Mike'], ['Logan', 'Jack'],
                      ['Mike', 'Alexander']]) is True,\
        'Grandfather'

    assert is_family([['Logan', 'Mike'], ['Logan', 'Jack'],
                      ['Mike', 'Logan']]) is False,\
        'Can you be a father to your father?'

    assert is_family([['Logan', 'Mike'], ['Logan', 'Jack'],
                      ['Mike', 'Jack']]) is False,\
        'Can you be a father to your brother?'

    assert is_family([['Logan', 'William'], ['Logan', 'Jack'],
                      ['Mike', 'Alexander']]) is False,\
        'Looks like Mike is stranger in Logan\'s family'
