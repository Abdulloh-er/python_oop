
class moster:
    def __init__ (self, name, level, nyawa):
        self.name = name
        self.level = level
        self.nyawa = nyawa
        print(f"moster {self.name} memasuki arena")

    def __str__ (self):
        status = "HIDUP"
        if self.nyawa < 0:
            status = "HAS BEEN SLAY"

        return f"[{self.name}] | NYAWA: {self.nyawa} | STATUS: {status}"

    def damaged(self, damage):
        self.nyawa -= damage
        print(f"{self.name} terkena {damage} damage")
        if self.nyawa == 0:
            print(f"hero {self.name} kill the enemy")
