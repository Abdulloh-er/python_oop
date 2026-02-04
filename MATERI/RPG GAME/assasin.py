from hero import hero

class assasin(hero):
    def __init__(self, name, level, hp, mana):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        super().__init__(self, name, level, hp, mana, role="assasin")

    def critical(self, target):
     dmg = 900
     print(f"{self.name} terkena {dmg} damage!!")
     target.atk(target)
     target.damaged(dmg)