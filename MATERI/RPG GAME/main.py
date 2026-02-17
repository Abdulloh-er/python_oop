from colorama import init, Fore, Back, Style
from hero import hero
from mage import mage
from fighter import fighter
from assasin import assasin
from monter import moster

init(autoreset=True)

print("================================")
print(Back.GREEN + Style.DIM + Back.LIGHTRED_EX + "TIM MEMASUKIN ARENA TEMPUR\n")

yuzhong = hero("yuzhong", 1, 2000, 0, "fighter")
gusion = hero("gusion", 1, 1900, 100, "assasin")
kadita = hero("kadita", 1, 1800, 160, "mage")

print("================================")

print(Back.GREEN + Style.DIM + Back.LIGHTRED_EX + "MONSTER MEMASUKIN ARENA TEMPUR\n")
lord = moster("THE LORD", 999, 999)

print("================================")

party = [yuzhong, gusion, kadita]

print(yuzhong)
print(gusion)
print(kadita)

print(Back.GREEN + Style.DIM + f"\n{len(party)} Pasukan siap bertempur")
print("================================")

running = True
while running:
    print(lord)
    print(Back.BLUE + "1. attack 2. heal 3. exit")
    
    try:
        aksi = int(input("PILIH AKSI : "))
    except:
        print("INPUT HARUS ANGKA!")
        continue

    # ATTACK
    if aksi == 1:
        dmg = 100

        yuzhong.atk(lord)
        gusion.atk(lord)
        kadita.atk(lord)

        # TOTAL DAMAGE KE LORD
        total_dmg = dmg * len(party)
        lord.damaged(total_dmg)

        print(f"LORD TERKENA TOTAL {total_dmg} DAMAGE!")

        # CEK LORD MATI
        if lord.nyawa <= 0:
            print("LORD TERELIMINASI")
            running = False

    # HEAL
    elif aksi == 2:
        yuzhong.lifesteal(50)
        lord.lifesteal(200)

    # EXIT
    elif aksi == 3:
        print("\nEND GAME")
        print("HASIL PERTANDINGAN")
        print(yuzhong)
        print(gusion)
        print(kadita)
        print("\n")
        print(lord)
        running = False

    else:
        print("AKSI TIDAK VALID!")

print("================================")
