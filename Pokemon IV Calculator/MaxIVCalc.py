from numpy import *
import random
import time

count = 0

class pokemon:
    def __init__(self, HP, ATK, DEF, SPA, SPD, SPE):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SPA = SPA
        self.SPD = SPD
        self.SPE = SPE

numb_array = zeros(6, dtype = str)
numb_list = []

numb1 = input("Please input HP IV > ")
numb2 = input("Please input ATK IV > ")
numb3 = input("Please input DEF IV > ")
numb4 = input("Please input SPA IV > ")
numb5 = input("Please input SPD IV > ")
numb6 = input("Please input SPE IV > ")

numb_list.append(numb1)
numb_list.append(numb2)
numb_list.append(numb3)
numb_list.append(numb4)
numb_list.append(numb5)
numb_list.append(numb6)


print(numb_list)

"""
pikachu = pokemon(0, 0, 0, 0, 0, 0)
bulbasaur = pokemon(31, 31, 31, 31, 31, 31)

childPokemon = pokemon(0, 0, 0, 0, 0, 0)

random_indices = random.sample(range(6), 3)

random_indices.sort()




# Create a list of the attribute names corresponding to the random indices
attribute_names = [attribute_name for i, attribute_name in enumerate(vars(pikachu)) if i in random_indices]

# Access the randomly selected attributes using their names
for attribute_name in attribute_names:
    attribute_value = getattr(pikachu, attribute_name)
    print(f"{attribute_name}: {attribute_value}")


if pikachu.HP == 31:
    print ("You already have perfect IV")

elif pikachu.HP < 31 or pikachu.ATK < 31 or pikachu.DEF < 31 or pikachu.SPA < 31:
    while pikachu.HP < 31 or pikachu.ATK < 31 or pikachu.DEF < 31 or pikachu.SPA < 31:
        pikachu.HP = random.randint(0, 31)
        print("HP: ", pikachu.HP)

        pikachu.ATK = random.randint(0, 31)
        print("ATK: ", pikachu.ATK)

        pikachu.DEF = random.randint(0, 31)
        print("DEF: ", pikachu.DEF)


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
    print ("Current SPA IV is", pikachu.SPA)
    print ("Current SPD IV is", pikachu.SPD)
    print ("Current SPE IV is", pikachu.SPE)
    """