"""
Liskov Substitution Principle

Uma subclasse deve ser substituível pela sua superclasse 
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, pernas: int):
        self.name = name
        self.pernas = pernas
    
    def get_name(self) -> str:
        return self.name

    def leg_count(self) -> int:
        return self.pernas
        

class AnimalBase(Animal):
    def __init__(self, name, pernas):
        super().__init__(name, pernas)

class Lion(Animal):
    def __init__(self):
        super().__init__('lion', 4)

class Snake(Animal):
    def __init__(self):
        super().__init__('snake', 0)


def animal_leg_count(animals: list):
    count = 0
    for animal in animals:
        count += animal.leg_count()
    return count


animais = [Snake(), Lion(), Animal('Teste', 10)]
animal_leg_count(animais)



