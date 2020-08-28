'''
https://py.checkio.org/en/mission/the-lancers/

... the vampires fought fiercely. Judging by the course of the battle, Sir
Ronald made the right decision, although not very ethically ambiguous.
Suddenly, new soldiers joined the Umbert’s ranks - has he really got an ace up
his sleeve? Lancers presented the fresh forces, which made Sir Ronald’s
position increasingly difficult, lancers could attack two soldiers at once with
their long spears. Something needed to be done with that…

It seems that the Warrior, Knight, Defender and Vampire are not enough to win
the battle. Let's add one more powerful unit type - the Lancer. Lancer should
be the subclass of the Warrior class and should attack in a specific way - when
he hits the other unit, he also deals a 50% of the deal damage to the enemy
unit, standing behind the firstly assaulted one (enemy defense makes the deal
damage value lower - consider this).

The basic parameters of the Lancer:

health = 50
attack = 6

Input: The warriors and armies.
Output: The result of the battle (True or False).

How it is used: For computer games development.
Precondition: 5 types of units
'''


# Taken from mission The Vampires

class Warrior:
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense

    def attacking(self, unit):
        unit.is_attacked(self)
        return None

    def is_attacked(self, unit, power=1):
        self.health -= (unit.attack * power) if unit.is_alive else 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3, defense=2)

    def is_attacked(self, unit, power=1):
        self.health -= max(0, (unit.attack * power) - self.defense)


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4, defense=0)
        self.vampirism = 50  # == %

    def attacking(self, unit):
        unit.is_attacked(self)
        if hasattr(unit, 'defense'):
            self.health += ((self.attack - unit.defense)
                            * self.vampirism) // 100
        return None


class Lancer(Warrior):
    def __init__(self):
        super().__init__(health=50, attack=6, defense=0)
        self.attack_nextunit = 50  # == %

    def attacking(self, unit):
        unit.is_attacked(self)
        attack_next_power = (self.attack * self.attack_nextunit) // 100
        return attack_next_power


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
    def next_waiting(self):
        return self.units[1] if len(self.units) > 1 else None

    @property
    def update_army(self):
        if self.units[0].health <= 0:
            self.units.pop(0)


class Battle():
    def __init__(self):
        pass

    def fight(self, army_a, army_b):
        while army_a.is_alive and army_b.is_alive:
            fight(army_a.next_battle, army_b.next_battle,
                  army_a.next_waiting, army_b.next_waiting)
            army_a.update_army
            army_b.update_army
        return army_a.is_alive


def fight(unit_a, unit_b, unit_a_waiting=None, unit_b_waiting=None):
    while unit_a.is_alive and unit_b.is_alive:
        fight_a_power = unit_a.attacking(unit_b)
        fight_b_power = unit_b.attacking(unit_a)
        if unit_b_waiting and fight_a_power:
            unit_b_waiting.is_attacked(unit_a, fight_a_power)
        elif unit_a_waiting and fight_b_power:
            unit_a_waiting.is_attacked(unit_b, fight_b_power)
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
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(freelancer, vampire) is True
    assert freelancer.is_alive is True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is True
    assert battle.fight(army_3, army_4) is False
