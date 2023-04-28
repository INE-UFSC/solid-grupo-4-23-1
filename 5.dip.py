"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""

"""
class Player:
    def __init__(self, name):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self, char: Player):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
"""

from abc import ABC, abstractmethod

class Char(ABC):
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp

    @property
    def hp(self):
        return self.__hp

    @property
    def name(self):
        return self.__name


class Player(Char):
    def __init__(self, name):
        super().__init__(name, 100)
        self.__speed = 1
        self.stats = StatsReporter(self)
        self.__name = name

    @property
    def speed(self):
        return self.__speed

class StatsReporter:
    def __init__(self, char: Char):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name}')
        print(f'HP:{self.char.hp}')

p = Player("p1")
p.stats.report()
