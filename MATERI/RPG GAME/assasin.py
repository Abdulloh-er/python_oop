from hero import hero

class assasin(hero):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp, mana, role="assasin")

    def critical(self, target):
        dmg = 900
        print(f"{self.name} memberikan CRITICAL {dmg} damage!!")
        target.atk(self)
        target.damaged(dmg)
