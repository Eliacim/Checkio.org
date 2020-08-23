# -*- coding: UTF-8 -*-

'''
https://py.checkio.org/en/mission/the-vampires/

The flocks of crows circled over the battlefield. Many brave warriors have
fallen in this battle, many have continued to fight. "If this goes on, we’ll
simply kill each other, and there will be no winners - we’ll all lose." -
reflected Sir Ronald, watching a bleak picture in front of him. "I have to make
an important decision. I know what it’ll cost, but now that’s the only thing
that can save us all..." A long time ago, when he was often in search of
trouble and adventure, he went to hunt a witch who had a huge bounty on her
head. The bloody creature was able to save her life by persuading the knight to
take a gift from her - a vial of vampire blood. This blood poured into the
dying man’s mouth could bring him back to life in vampire form. Is it really
the day when he has to use it?.. It seemed to be the only way to win this
battle. Sir Ronald began to lean over the barely living bodies of his knights,
who were lying beside him. To each of them he said:
- "Drink. You’ll be given a new life..."


So we have 3 types of units: the Warrior, Knight and Defender. Let's make the
battles even more epic and add another type - the Vampire! Vampire should be
the subclass of the Warrior class and have the additional vampirism parameter,
which helps him to heal himself. When the Vampire hits the other unit, he
restores his health by +50% of the dealt damage (enemy defense makes the dealt
damage value lower).

The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%

You should store vampirism attribute as an integer (50 for 50%). It will be
needed to make this solution evolutes to fit one of the next challenges of this
saga.

Input: The warriors and armies.
Output: The result of the battle (True or False).

How it is used: For the computer games development.
Precondition: 4 types of units
'''


# Taken from mission The Defenders

class Warrior:
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense

    def attacking(self, unit):
        unit.is_attacked(self)

    def is_attacked(self, unit):
        self.health -= unit.attack if unit.is_alive else 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3, defense=2)

    def is_attacked(self, unit):
        self.health -= max(0, unit.attack - self.defense)


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4, defense=0)
        self.vampirism = 50

    def attacking(self, unit):
        unit.is_attacked(self)
        if hasattr(unit, 'defense'):
            self.health += ((self.attack - unit.defense)
                            * self.vampirism) // 100


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, type, qty):
        for q in range(qty):
            self.units.append(type())

    @property
    def total_alive(self):
        return len(self.units)

    @property
    def is_alive(self):
        return self.total_alive > 0

    @property
    def next_battle(self):
        return self.units[0]

    @property
    def update_army(self):
        if self.units[0].health <= 0:
            self.units.pop(0)


class Battle():
    def __init__(self):
        pass

    def fight(self, army_a, army_b):
        while army_a.is_alive and army_b.is_alive:
            fight(army_a.next_battle, army_b.next_battle)
            army_a.update_army
            army_b.update_army
        return army_a.is_alive


def fight(unit_a, unit_b):
    while unit_a.is_alive and unit_b.is_alive:
        unit_a.attacking(unit_b)
        unit_b.attacking(unit_a)
    return unit_a.is_alive


if __name__ == '__main__':
    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
    assert fight(bob, mike) is False
    assert fight(lancelot, rog) is True
    assert fight(eric, richard) is False
    assert fight(ogre, adam) is True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    army_1 = Army()
    army_1.add_units(Defender, 5)
    army_1.add_units(Vampire, 6)
    army_1.add_units(Warrior, 7)

    army_2 = Army()
    army_2.add_units(Warrior, 6)
    army_2.add_units(Defender, 6)
    army_2.add_units(Vampire, 6)

    battle = Battle()

    assert battle.fight(army_1, army_2) is False
    assert battle.fight(my_army, enemy_army) is False
    assert battle.fight(army_3, army_4) is True
