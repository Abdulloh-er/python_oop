class Hero:
    def __init__(self, name, hp, level, mana, role="hero"):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.level = level
        self.mana = mana
        self.role = role

        self.rage = False

        print(self.name, "masuk arena sebagai", self.role)

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def attack(self, enemy, damage):
        if self.is_alive() == False:
            print(self.name, "sudah mati, tidak bisa menyerang")
            return

        if damage <= 0:
            print("Damage tidak boleh 0 atau negatif")
            return

        # bonus berdasarkan role
        if self.role == "Mage":
            damage = damage + 10

        # Rage Mode untuk Boss
        if self.role == "Boss" and self.hp <= self.max_hp / 2:
            if self.rage == False:
                print("😈 Raja Iblis masuk RAGE MODE!")
                self.rage = True

            print("🔥 Boss melakukan CRITICAL HIT!")
            damage = damage * 2

        print(self.name, "menyerang", enemy.name, "damage", damage)
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp = self.hp - damage

        if self.hp < 0:
            self.hp = 0

        print(self.name, "kena", damage, "damage. HP:", self.hp)

        if self.hp == 0:
            print(self.name, "mati!")

    def heal(self):
        if self.is_alive() == False:
            print(self.name, "sudah mati, tidak bisa heal")
            return

        if self.mana <= 0:
            print(self.name, "tidak punya mana untuk heal")
            return

        heal = 10

        # bonus heal untuk Healer
        if self.role == "Healer":
            heal = 25

        self.hp = self.hp + heal
        self.mana = self.mana - 5

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(self.name, "heal", heal, "| HP:", self.hp, "| Mana:", self.mana)



#parttyyyy