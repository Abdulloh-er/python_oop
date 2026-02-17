from hero import hero

class mage(hero):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp, mana, role="mage")

    def critical(self, target):
        dmg = 900
        print(f"{self.name} memberikan MAGIC CRITICAL {dmg} damage!!")
        target.atk(self)
        target.damaged(dmg)
