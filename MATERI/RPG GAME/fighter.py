from hero import hero

class fighter(hero):
    def __init__(self, name, level, hp, mana):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        super().__init__(self, name, level, hp, mana, role="fighter")

    def critical(self, target):
     dmg = 1900
     print(f"{self.name} terkena {dmg} damage!!")
     target.atk(target)
     target.damaged(dmg)