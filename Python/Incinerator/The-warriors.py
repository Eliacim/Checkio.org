'''
https://py.checkio.org/en/mission/the-warriors/

I'm sure that many of you have some experience with computer games. But have
you ever wanted to change the game so that the characters or a game world would
be more consistent with your idea of the perfect game? Probably, yes. In this
mission (and in several subsequent ones, related to it) you’ll have a chance
"to sit in the developer's chair" and create the logic of a simple game about
battles. Let's start with the simple task - one-on-one duel.

You need to create the class Warrior, the instances of which will have:

2 parameters - health (equal to 50 points) and attack (equal to 5 points)

1 property - is_alive, which can be True (if warrior's health is > 0) or False
(in the other case).

In addition you have to create the second unit type - Knight, which should be
the subclass of the Warrior but have the increased attack - 7.

Also you have to create a function fight(), which will initiate the duel
between 2 warriors and define the strongest of them.

The duel occurs according to the following principle:

Every turn, the first warrior will hit the second and this second will lose his
health in the same value as the attack of the first warrior.

After that, if he is still alive, the second warrior will do the same to the
first one.

The fight ends with the death of one of them. If the first warrior is still
alive (and thus the other one is not anymore), the function should return True,
False otherwise.

Input: The warriors.
Output: The result of the duel (True or False).

Precondition:

2 types of units All given fights have an end (for all missions).
'''


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def attacked(self, unit):
        self.health -= unit.attack if unit.is_alive else 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.attacked(unit_1)
        unit_1.attacked(unit_2)
    return unit_1.is_alive


if __name__ == '__main__':

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
