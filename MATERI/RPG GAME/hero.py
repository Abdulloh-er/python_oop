#rpg game

class hero:
    def __init__ (self, name, level, hp, mana, role):
        self.name = name
        self.level = level
        self.__hp = hp
        self.mana = mana
        self.role = role
        print(f"SPAWN {self.role}")

    def __str__ (self):
        status = "HIDUP"
        if self.__hp == 0:
            status = "HAS BEEN SLAY"

        return f"[{self.role}] | {self.name} | HP: {self.__hp} | STATUS: {status}"

    def damaged(self, damage):
        self.__hp -= damage
        print(f"{self.name} terkena {damage} damage")
        if self.hp == 0:
            print(f"hero {self.name} kill the enemy")

    def atk(self, atk):
        print(f"{self.name} Menyerang")

    def lifesteal(self, amount):
        self.hp += amount
        print(f"{self.name} is praying")

    #bag 2
    def critical(self, target):
     dmg = 1900
     print(f"{self.name} terkena {dmg} damage!!")
     target.atk(target)
     target.damaged(dmg)




    def get_hp(self):
        return self.__hp
    
    def set_hp(self, add_hp):
        self.__hp += add_hp




     