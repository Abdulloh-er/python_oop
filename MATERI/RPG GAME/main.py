from hero import hero
from mage import mage
from fighter import fighter
from assasin import assasin
from monter import moster

print("================================")
print("TIM MEMASUKIN ARENA TEMPUR\n")
yuzhong = hero("yuzhong", 1, 2000, 0, "fighter")
gusion = hero("gusion", 1, 1900, 100, "assasin")
kadita = hero("kadita", 1, 1800, 160, "mage")
print("================================")

print("MONSTER MEMASUKIN ARENA TEMPUR\n")
lord = moster("THE LORD", 999, 999)
print("================================")

party = [
    yuzhong,
    gusion,
    kadita
]
print(f"{len(party)} Pasukan siap bertempur")
print("================================")

# print("PERANG DI MULAI\n")
# print(yuzhong)
# print(f"darah yuzhong {yuzhong.get_hp()}")
# yuzhong.set_hp(1000)
# print(gusion)
# print(kadita)
# print("\n")
# print(lord)

running = True
while running:
    print(lord)
    print("1. attack 2. heal 3. exit")
    aksi = int(input("PILIH AKSI : "))

    if aksi == 1:
        dmg = 100
        yuzhong.atk(lord)
        gusion.atk(lord)
        kadita.atk(lord)
        lord.damaged(dmg * 4)

        if (lord.nyawa == 0):
            print("LORD TERELIMINASI")
            running = False

    elif aksi == 2:
        yuzhong.lifesteal(50)
     
    elif aksi == 3:
        print("END GAME")
        print("HASIL PERTANDINGAN")
        print(yuzhong)
        print(gusion)
        print(kadita)
        print("\n")
        print(lord)
print("================================")


