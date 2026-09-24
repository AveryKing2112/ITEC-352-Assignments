"""
Main routine that demonstrates the Knight class form objects.py
Avery King
ITEC-352-001
9/14/2026
"""
# Import Knight class from the objects module
from objects import Knight, cavalryKnight, darkKnight



def main():
    # create two Knight objects with starting health and armor_rating
    lancelot = darkKnight("Lancelot", 100, 10)
    mordred = cavalryKnight("Mordred", 90, 10)

    # Have each knight attack the other to demonstrate object interaction
    lancelot.deal_damage(mordred, 15)
    mordred.deal_damage(lancelot, 10)

if __name__ == "__main__":
    main()