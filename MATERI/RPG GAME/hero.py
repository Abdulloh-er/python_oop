# RPG GAME 
from __future__ import annotations
from monter import moster

class hero:
    def __init__(self, name: str, level: int, hp: int, mana: int, role: str):
        self.name = name
        self.level = level
        self.__hp = hp
        self.mana = mana
        self.role = role
        print(f"SPAWN {self.role}")

    def __str__(self):
        status = "HIDUP"
        if self.__hp <= 0:
            status = "HAS BEEN SLAY"

        return f"[{self.role}] | {self.name} | HP: {self.__hp} | STATUS: {status}"

    # GETTER HP
    def get_hp(self):
        return self.__hp

    # SETTER / TAMBAH HP
    def set_hp(self, add_hp):
        self.__hp += add_hp
        if self.__hp < 0:
            self.__hp = 0

    # DAMAGED
    def damaged(self, damage: int):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0

        print(f"{self.name} terkena {damage} damage")

        if self.__hp == 0:
            print(f"hero {self.name} HAS BEEN SLAY")

    # ATTACK
    def atk(self, target: moster):
        print(f"{self.name} Menyerang {target.name}")

    # LIFESTEAL
    def lifesteal(self, amount: int):
        self.set_hp(amount)
        print(f"{self.name} is praying +{amount} HP")

    # CRITICAL ATTACK
    def critical(self, target):
        dmg = 1900
        print(f"{self.name} memberikan CRITICAL {dmg} damage!!")
        target.atk(self)
        target.damaged(dmg)
