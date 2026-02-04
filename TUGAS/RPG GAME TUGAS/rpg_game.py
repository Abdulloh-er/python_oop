class Hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        self.name = name
        self.job = job
        self.hp = hp
        self.type = hero_type
        print(f"✨ {self.name} memasuki arena!")

    def is_alive(self):
        return self.hp > 0
    

    def attack(self, enemy, damage):
        # hero harus hidup
        if not self.is_alive():
            print(f"💀 {self.name} sudah mati dan tidak bisa menyerang.")
            return

        # damage harus valid
        if damage <= 0:
            print("❌ Damage harus lebih dari 0.")
            return

        print(f"⚔️ {self.name} menyerang {enemy.name} ({damage} damage)")
        enemy.take_damage(damage)

        # boss rage mode (simple)
        if enemy.type == "boss" and enemy.hp <= 50 and enemy.is_alive():
            print(f"🔥 {enemy.name} menjadi MARAH! (Rage Mode)")

    def take_damage(self, damage):
        self.hp -= damage

        # hp tidak boleh minus
        if self.hp < 0:
            self.hp = 0

        print(f"🩸 {self.name} terkena {damage} damage. HP: {self.hp}")

        # jika mati
        if self.hp == 0:
            print(f"☠️ {self.name} mati.")

    def heal(self):
        # tidak bisa heal kalau mati
        if not self.is_alive():
            print(f"💀 {self.name} sudah mati dan tidak bisa heal.")
            return

        # heal simple berdasarkan role
        if self.job == "support":
            heal_amount = 25
        elif self.job == "tank":
            heal_amount = 15
        else:
            heal_amount = 20

        self.hp += heal_amount
        print(f"💚 {self.name} heal +{heal_amount}. HP: {self.hp}")




print("\nMalam itu arena sepi, tapi tiga hero malah dateng kayak janjian mau mabar.\n")

paquito = Hero("Paquito", "fighter", 120)
gusion  = Hero("Gusion", "mage", 90)
ling    = Hero("Ling", "assassin", 80)

zombie = Hero("Zombie", "monster", 60, hero_type="monster")
lord   = Hero("Lord", "boss", 150, hero_type="boss")

print("\nZombie muncul pelan-pelan, jalannya kayak orang belum ngopi.")
paquito.attack(zombie, 25)
gusion.attack(zombie, 30)
ling.attack(zombie, 20)

print("\nZombie gak terima, langsung nyeruduk siapa aja yang deket.")
zombie.attack(paquito, 15)
zombie.attack(gusion, 10)

print("\nTiba-tiba tanah geter. Lord turun ke arena, bikin suasana jadi gak santai.")
paquito.attack(lord, 20)
gusion.attack(lord, 35)
ling.attack(lord, 30)

print("\nLord mulai naik darah. Pukulan asal, yang penting kena.")
lord.attack(paquito, 25)
lord.attack(ling, 40)

print("\nPara hero mulai ngos-ngosan. Mereka nyempetin diri buat tarik napas dan heal.")
paquito.heal()
gusion.heal()
ling.heal()

print("\nPertarungan terakhir. Gak ada mikir strategi, yang penting hajar dulu.")
paquito.attack(lord, 30)
gusion.attack(lord, 40)
ling.attack(lord, 35)

print("\nArena hancur lebur. Entah siapa yang menang, yang jelas saya capek.")