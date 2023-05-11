from numpy import *
import random
import time

################## DEFINE STUFF ############################

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
    def __init__(self, ivList): # assign each element in the list/array as an attribute for the class
        self.HP = ivList[0]
        self.ATK = ivList[1]
        self.DEF = ivList[2]
        self.SPA = ivList[3]
        self.SPD = ivList[4]
        self.SPE = ivList[5]

ivList1 = [] #pokemon 1
ivList2 = [] #pokemon 2


count = 0 # just counter things

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

# Set the lists to arrays to manipulate elements easier
iv1array = array(ivList1)
iv2array  = array(ivList2)

# choose 3 random numbers between 1 and 6 (but elements 0 to 5)
selectedIV = random.sample(range(6), 3)
notSelectedIV = [i for i in range(6) if i not in selectedIV] # this checks if the numbers are inside selectedIV or not. If it's not, then it creates a new list of notSelectedIV

print(selectedIV)

ivList3 = [iv1array[selectedIV[0]], iv1array[selectedIV[1]], iv1array[selectedIV[1]],
           iv2array[selectedIV[0]], iv2array[selectedIV[1]], iv2array[selectedIV[2]]] #pokemon 3

random.shuffle(notSelectedIV)
ivList3[notSelectedIV[0]] = random.randint(0, 31)
ivList3[notSelectedIV[1]] = random.randint(0, 31)
ivList3[notSelectedIV[2]] = random.randint(0, 31)

print(ivList3)

# Test print to see if the lists are working

#print("Pokemon 1's IV is", iv1array)
#print("Pokemon 2's IV is", iv2array)

#pokeParent1 = pokemon(iv1array)
#pokeParent2 = pokemon(iv2array)


"""

print(pokeParent1.HP)
print(pokeParent1.ATK)
print(pokeParent1.DEF)
print(pokeParent1.SPA)
print(pokeParent1.SPD)
print(pokeParent1.SPE)

print(pokeParent2.HP)
print(pokeParent2.ATK)
print(pokeParent2.DEF)
print(pokeParent2.SPA)
print(pokeParent2.SPD)
print(pokeParent2.SPE)


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