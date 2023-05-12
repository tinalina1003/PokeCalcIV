import numpy as np
import random

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

# a counter to count how many 31's are in each pokemon's IV list
def perfCount(perfectCounter, ivList):
    for stats in ivList:
        if stats == 31:
            perfectCounter += 1
    return perfectCounter


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
parent1PerfCount = 0 # parent 1's perfect IV count
parent2PerfCount = 0 # parent 2's perfect IV count
childPerfCount  = 0 # child's perfect IV count

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

counter =  0

# this an array of all 31s. Use this to check
def all_thirtyones(numbers):
    return all(num == 31 for num in numbers)


################# MAIN CODE ##########################

### NEED TO CREATE DESTINY KNOT####

# Call the inputFunc function twice, once for each Pokemon. This sets initial conditions
inputFunc(ivList1, pokemon1)
inputFunc(ivList2, pokemon2)

# Set the lists to arrays to manipulate elements easier
iv1array = np.array(ivList1)
iv2array  = np.array(ivList2)


# choose 3 random numbers between 1 and 6 (but elements 0 to 5)
selectedIV = random.sample(range(6), 3)
notSelectedIV = [i for i in range(6) if i not in selectedIV] # this checks if the numbers are inside selectedIV or not. If it's not, then it creates a new list of notSelectedIV

print("Elements", np.sort(selectedIV), "are passed down to offspring") # sort to make it easier to look at elements

iv3array = [iv1array[selectedIV[0]], iv1array[selectedIV[1]], iv1array[selectedIV[1]],
           iv2array[selectedIV[0]], iv2array[selectedIV[1]], iv2array[selectedIV[2]]] # pokemon 3 array

random.shuffle(notSelectedIV)
iv3array[notSelectedIV[0]] = random.randint(0, 31)
iv3array[notSelectedIV[1]] = random.randint(0, 31)
iv3array[notSelectedIV[2]] = random.randint(0, 31)

# I need to set this as an array to manipulate
iv3array = np.array(iv3array)

print(iv3array)

# Test print to see if the lists are working

# convert attributes to array
pokeParent1 = pokemon(iv1array)
pokeParent2 = pokemon(iv2array)
pokeChild  = pokemon(iv3array)


###### MAKE IT SO THAT THE CHILD COUNT OF 31'S WILL REPLACE THAT OF PARENTS ####

perfCount(parent1PerfCount, iv1array)
perfCount(parent2PerfCount, iv2array)
perfCount(childPerfCount, iv3array)

if perfCount(childPerfCount, iv3array) > perfCount(parent1PerfCount, iv1array):
    iv1array = iv3array

else:
    iv2array = iv3array

print("New Stats")
print(iv1array)
print(iv2array)
























"""

############  CODE NOT WORKING ####################
######## WILL  NEED TO MAKE IT SO IT STILL PASSES ON THE 3 ATTRIBUTES  ############
if pokeChild.HP == 31 and pokeChild.ATK == 31 and pokeChild.DEF == 31  and pokeChild.SPA == 31 and pokeChild.SPD == 31 and pokeChild.SPE == 31:
    print("You have perfect IV pokemon!")

elif pokeChild.HP < 31 or pokeChild.ATK < 31 or pokeChild.DEF < 31  or pokeChild.SPA < 31 or pokeChild.SPD < 31 or pokeChild.SPE < 31:
    while pokeChild.HP < 31 or pokeChild.ATK < 31 or pokeChild.DEF < 31  or pokeChild.SPA < 31 or pokeChild.SPD < 31 or pokeChild.SPE < 31:
        pokeChild.HP = random.randint(0, 31)
        pokeChild.ATK = random.randint(0, 31)
        pokeChild.DEF = random.randint(0, 31)
        pokeChild.SPA = random.randint(0, 31)
        pokeChild.SPD = random.randint(0, 31)
        pokeChild.SPE = random.randint(0, 31)
        count += 1
        print(count)

attrs_as_array = list(pokeChild.__dict__.values())
print(attrs_as_array)

if ivList3[i] == 31:
    print ("You already have perfect IV")

elif ivList3[i]:
        while pokeParent1.HP < 31 and pokeParent1.ATK < 31 and pokeParent1.DEF < 31 and pokeParent1.SPA < 31:
            pokeParent1.HP = random.randint(0, 31)
            print("HP: ", pokeParent1.HP)

            pokeParent1.ATK = random.randint(0, 31)
            print("ATK: ", pokeParent1.ATK)

            pokeParent1.DEF = random.randint(0, 31)
            print("DEF: ", pokeParent1.DEF)


elif pokeParent1.HP < 31 and pokeParent1.ATK < 31 and pokeParent1.DEF < 31 and pokeParent1.SPA < 31 and pokeParent1.SPD < 31 and pokeParent1.SPE < 31:
    while pokeParent1.HP < 31 and pokeParent1.ATK < 31 and pokeParent1.DEF < 31 and pokeParent1.SPA < 31 and pokeParent1.SPD < 31 and pokeParent1.SPE < 31:

        pokeParent1.HP = random.randint(0, 31)
        print("HP: ", pokeParent1.HP)

        pokeParent1.ATK = random.randint(0, 31)
        print("ATK: ", pokeParent1.ATK)

        pokeParent1.DEF = random.randint(0, 31)
        print("DEF: ", pokeParent1.DEF)

        pokeParent1.SPA = random.randint(0, 31)
        print("SPA: ", pokeParent1.SPA)

        pokeParent1.SPD = random.randint(0, 31)
        print("SPD: ", pokeParent1.SPD)

        pokeParent1.SPE = random.randint(0, 31)
        print("SPE: ", pokeParent1.SPE)

        count += 1

    print ("You got max IV after", count ,"tries!")
    print ("Current HP IV is", pokeParent1.HP)
    print ("Current ATK IV is", pokeParent1.ATK)
    print ("Current DEF IV is", pokeParent1.DEF)
    print ("Current SPA IV is", pokeParent1.SPA)
    print ("Current SPD IV is", pokeParent1.SPD)
    print ("Current SPE IV is", pokeParent1.SPE)
"""