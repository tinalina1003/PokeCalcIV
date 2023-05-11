from numpy import *
import random
import time

################## DEFINE STUFF ############################
count = 0

def inputFunc(inputList, pokeParents):
    for inputVals in pokeParents:
        while True:
            pokeIV1 = input(inputVals)

            if pokeIV1 == "perfect":
                inputList.append(31) #appends to the different lists
                break # break out of the while loop and goes to the next index

            elif pokeIV1 in ["no good", "decent", "pretty good", "very good", "fantastic"]:
                inputList.append(0) #appends to the different lists
                break # break out of the while loop and goes to  the next index

            else:
                print("Please input a value IV") #this loop will continue forever on index inputVals until a valid input is received

class pokemon:
    def __init__(self, HP, ATK, DEF, SPA, SPD, SPE):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SPA = SPA
        self.SPD = SPD
        self.SPE = SPE

ivList1 = [] #pokemon 1
ivList2 = [] #pokemon 2
ivList3 = [] #pokemon 3   

pokemon1 = [ "Please input HP IV for first pokemon > ",
            "Please input ATK IV for first pokemon  > ",
            "Please input DEF IV for first pokemon  > ",
            "Please input SPA IV for first pokemon  > ",
            "Please input SPD IV for first pokemon  > ",
            "Please input SPE IV for first pokemon  > "]

pokemon2 = [ "Please input HP IV for second pokemon > ",
            "Please input ATK IV for second pokemon  > ",
            "Please input DEF IV for second pokemon  > ",
            "Please input SPA IV for second pokemon  > ",
            "Please input SPD IV for second pokemon  > ",
            "Please input SPE IV for second pokemon  > "]

################# MAIN CODE ##########################

# Call the inputFunc function twice, once for each Pokemon
inputFunc(ivList1, pokemon1)
inputFunc(ivList2, pokemon2)

# Test print to see if the lists are working
print(ivList1)
print(ivList2)



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