class moster:
    def __init__(self, name, level, nyawa):
        self.name = name
        self.level = level
        self.nyawa = nyawa
        print(f"moster {self.name} memasuki arena")

    def __str__(self):
        status = "HIDUP"
        if self.nyawa <= 0:
            status = "HAS BEEN SLAY"

        return f"[{self.name}] | NYAWA: {self.nyawa} | STATUS: {status}"

    def damaged(self, damage):
        self.nyawa -= damage
        if self.nyawa < 0:
            self.nyawa = 0

        print(f"{self.name} terkena {damage} damage")

        if self.nyawa == 0:
            print(f"moster {self.name} HAS BEEN SLAY")

    # HEAL / LIFESTEAL MONSTER
    def lifesteal(self, amount):
        self.nyawa += amount
        print(f"{self.name} is praying +{amount} NYAWA")
