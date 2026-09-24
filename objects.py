"""
Contains the Knight class for main.py
Avery King
ITEC-352-001
9/14/2026
"""

#Using dataclasses instead of hard coding __init__
from dataclasses import dataclass

#Defining the Knight class with 3 attributes and 2 methods
@dataclass
class Knight:
    name: str
    health: float
    armor_rating: float


    #Method that that reduces health when the knight takes damage
    def take_damage(self, amount):
        reduced_amount = max(amount - self.armor_rating, 0)
        self.health = self.health - reduced_amount
        print(f"{self.name} took {reduced_amount} damage (armor absorbed {amount - reduced_amount}). Health is now {self.health}.")

    #Method that has this knight attack another knight, dealing damage
    def deal_damage(self, target, amount):
        print(f"{self.name} attacks {target.name} for {amount} damage!")
        target.take_damage(amount)


@dataclass
class cavalryKnight(Knight):
    charge_bonus:float = 0.0

    # Ovverdies knight deal_damage adds the charge bonus to the attack
    def deal_damage(self, target, amount):
        print(f"{self.name} charges on horseback!")
        super().deal_damage(target, amount + self.charge_bonus)





@dataclass
class darkKnight(Knight):
    dark_magic:float = 25.0
    # Ovverides Knight deal_damage normal attack, then dark magic that ignores armro
    def deal_damage(self, target, amount):
        target.health -= self.dark_magic
        super().deal_damage(target, amount)
        print(f"{self.name} casts dark magic {self.dark_magic} onto {target.name}. health is now {target.health}")
