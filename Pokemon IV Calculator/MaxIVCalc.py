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
        self.HP, self.ATK, self.DEF, self.SPA, self.SPD, self.SPE = ivList

ivList1 = [] #pokemon 1
ivList2 = [] #pokemon 2
ivList3 = [0, 0, 0, 0, 0, 0] #initialize pokemon
perfectList = [31, 31, 31, 31, 31, 31] # perfect IV list to check with

counter =  0 # just counter things
parent1PerfCount = 0 # parent 1's perfect IV count
parent2PerfCount = 0 # parent 2's perfect IV count
childPerfCount  = 0 # child's perfect IV count

pokemon1 = [f"Please input {stat} IV for first pokemon > " for stat in ["HP","ATK","DEF","SPA","SPD","SPE"]] # formatted string which if you put in {} will replace whats in the list into there
pokemon2 = [f"Please input {stat} IV for second pokemon > " for stat in ["HP","ATK","DEF","SPA","SPD","SPE"]]


################# MAIN CODE ##########################

### NEED TO CREATE DESTINY KNOT####
destinyKnot = False

while destinyKnot == False:
    DK = input("Do you have destiny knot? [y/n] ")
    if DK == "y":
        destinyKnot = True

    elif DK == "n":
        destinyKnot = True
    else:
        print("Please input a correct input")

# Call the inputFunc function twice, once for each Pokemon. This sets initial conditions
inputFunc(ivList1, pokemon1)
inputFunc(ivList2, pokemon2)

"""print(ivList1)
print(ivList2)"""


# check if either of the iv lists matches max IV
while ivList1 != perfectList and ivList2 != perfectList:
    # choose 3 random numbers between 1 and 6 (but elements 0 to 5)
    selectedIV = random.sample(range(6), 3 if DK == "n" else 5) # 3 if default, 5 with destiny knot
    notSelectedIV = list(set(range(6)) - set(selectedIV)) # this gets the list of notSelectedIV's indices by the ones that are not in selectedIV

    print("Elements", np.sort(selectedIV), "are passed down to offspring") # sort to make it easier to look at elements


    ivList3 = [ivList1[selectedIV[0]], ivList1[selectedIV[1]], ivList1[selectedIV[2]],
            ivList2[selectedIV[0]], ivList2[selectedIV[1]], ivList2[selectedIV[2]]] # pokemon 3 array

    for i in range(len(notSelectedIV)):
        ivList3[notSelectedIV[i]] = random.randint(0, 31)

    print("The child pokemon's stats are ", ivList3)

    if ivList3 == perfectList:
        break
    else:
        ###### MAKE IT SO THAT THE CHILD COUNT OF 31'S WILL REPLACE THAT OF PARENTS ####
        perfCount(parent1PerfCount, ivList1)
        perfCount(parent2PerfCount, ivList2)
        perfCount(childPerfCount, ivList3)

        if perfCount(childPerfCount, ivList3) == perfCount(parent2PerfCount, ivList2) and perfCount(parent1PerfCount, ivList1):
            for i in range(len(ivList3)):
                if ivList3[i] > ivList2[i] or ivList3[i] > ivList1[i]:
                    lowerNum = min(ivList1[i], ivList2[i])
                    if lowerNum == ivList1[i]:
                        ivList1 = ivList3
                        print("Replaced first pokemon")
                        break
                    else:
                        ivList2 = ivList3
                        print("Replaced second pokemon")
                        break
            


        if perfCount(childPerfCount, ivList3) > perfCount(parent1PerfCount, ivList1):
            ivList1 = ivList3

        if perfCount(childPerfCount, ivList3) > perfCount(parent2PerfCount, ivList2):
            ivList2 = ivList3

        print("New Stats")
        print("This is pokemon 1's stats", ivList1)
        print("This is pokemon 2's stats", ivList2)
        print("--------------------------------------------------")

        counter += 1

print("Congrats! It took ", counter,"number of eggs")    

