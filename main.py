"""
Main routine that demonstrates the Knight class form objects.py
Avery King
ITEC-352-001
9/14/2026
"""
# Import Knight class from the objects module
from objects import Knight



def main():
    # create two Knight objects with starting health and armor_rating
    lancelot = Knight("Lancelot", 100, 5)
    mordred = Knight("Mordred", 90, 3)

    # Have each knight attack the other to demonstrate object interaction
    lancelot.deal_damage(mordred, 15)
    mordred.deal_damage(lancelot, 10)

if __name__ == "__main__":
    main()