#ngulang dikit
print("HELLO WORLD\n")


#bikin fungsi 

def halo(nama):
    print("Halo " + nama)  

halo("Andi")
halo("Budi")


def nilai(nama, sem1, sem2):
    rumus = sem1 + sem2 
    print(f"nilai total: {nama}: {rumus}")

nilai("Andi", 80, 90)
nilai("Budi", 70, 85)
nilai("Caca", 75, 95)

#oop

print("Hello World")

#definisikan kelas cat
class Cat:
    def __init__(self, color, age):
        self.color = color
        self.age = age

#object dari kelas cat
garfield = Cat("orange", 50)
bogor = Cat("black", 38)

print("object garfield:", garfield)
print("object bogor:", bogor)

print("warna garfield:", garfield.color)
print("umur garfield:", garfield.age)
    