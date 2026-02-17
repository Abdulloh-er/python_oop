from hero import hero

class fighter(hero):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp, mana, role="fighter")

    def critical(self, target):
        dmg = 1900
        print(f"{self.name} memberikan CRITICAL {dmg} damage!!")
        target.atk(target)
        target.damaged(dmg)
