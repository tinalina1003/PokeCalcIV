from numpy import *
import random
import time

count = 0

class pokemon:
    def __init__(self, name, HP, ATK, DEF, SPA, SPD, SPE):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SPA = SPA
        self.SPD = SPD
        self.SPE = SPE

pikachu = pokemon("Pikachu", 0, 0, 0, 0, 0, 0)
bulbasaur = pokemon("Bulbasaur", 31, 31, 31, 31, 31, 31)

if pikachu.HP == 31:
    print ("You already have perfect IV")

elif pikachu.HP < 31 or pikachu.ATK < 31 or pikachu.DEF < 31 or pikachu.SPA < 31 or pikachu.SPD < 31 or pikachu.SPE < 31:
    while pikachu.HP < 31 or pikachu.ATK < 31 or pikachu.DEF < 31 or pikachu.SPA < 31 or pikachu.SPD < 31 or pikachu.SPE < 31:

        pikachu.HP = random.randint(0, 31)
        print("HP: ", pikachu.HP)

        pikachu.ATK = random.randint(0, 31)
        print("ATK: ", pikachu.ATK)

        pikachu.DEF = random.randint(0, 31)
        print("DEF: ", pikachu.DEF)

        pikachu.SPA = random.randint(0, 31)
        print("SPA: ", pikachu.SPA)

        pikachu.SPD = random.randint(0, 31)
        print("SPD: ", pikachu.SPD)

        pikachu.SPE = random.randint(0, 31)
        print("SPE: ", pikachu.SPE)

        count += 1

    print ("You got max IV after", count ,"tries!")
    print ("Current HP IV is", pikachu.HP)
    print ("Current ATK IV is", pikachu.ATK)
    print ("Current DEF IV is", pikachu.DEF)
    print ("Current 