import numpy as np
import random
import matplotlib.pyplot as plt

################## DEFINE STUFF ############################
# used for testing
data = np.loadtxt('E:/Python Projects/Pokemon IV Calculator/testStats.txt', dtype = int)
stats1 = data[:, 0]
stats2 = data[:, 1]


class pokemon(object):
    def __init__ (self, stats):
        self.stats = stats

def perfectIVCount(list):
    perfectCounter = 0
    for iv in list:
        if iv == 31:
            perfectCounter += 1
    return(perfectCounter)

def lowerNum(list1, list2, list3):
    if list3 > list1 and list3 > list2:

        minNum = min(list1, list2)
    return(minNum)

startMaleStats = {'HP': stats1[0],
                     'ATK': stats1[1],
                     'DEF': stats1[2],
                     'SPA': stats1[3],
                     'SPD': stats1[4],
                     'SPE': stats1[5],
                     }
startFemaleStats = {'HP': stats2[0],
                     'ATK': stats2[1],
                     'DEF': stats2[2],
                     'SPA': stats2[3],
                     'SPD': stats2[4],
                     'SPE': stats2[5],
                     }

offspringStats = {'HP': 0,
                     'ATK': 0,
                     'DEF': 0,
                     'SPA': 0,
                     'SPD': 0,
                     'SPE': 0,
                     }

perfectStats = {'HP': 31,
                     'ATK': 31,
                     'DEF': 31,
                     'SPA': 31,
                     'SPD': 31,
                     'SPE': 31,
                     }

# set methods as variables (think of methods as a return... returns something but you must set it to a variable before you can use it)
maleAllStats = pokemon(startMaleStats)
femaleAllStats = pokemon(startFemaleStats)
offspringAllStats = pokemon(offspringStats)
perfectStats = pokemon(perfectStats)

# extract stat names and values of male and female
statNames = list(perfectStats.stats.keys())
maleIVs = list(maleAllStats.stats.values())
femaleIVs = list(femaleAllStats.stats.values())
offspringIVs = list(offspringAllStats.stats.values())
perfectIVs = list(perfectStats.stats.values())

destinyKnot = False



while destinyKnot == False:
    DK = input('Do you have destiny knot? [y/n] > ')
    if DK == 'y':
        destinyKnot == True
        break
    elif DK  =='n':
        destinyKnot == True
        break
    else:
        print('Please input a valid input')



for i in range(10):
    while offspringIVs != perfectIVs:

        eggCount = 0

        if perfectIVCount(maleIVs) < 4 and perfectIVCount(femaleIVs) < 4:
            DK = 'n'

        selectedIV = np.sort(random.sample(range(6), 3 if DK == 'n' else 5)) # 3 if default, 5 with destiny knot
        notSelectedIV = np.sort(list(set(range(6)) - set(selectedIV))) # this gets the list of notSelectedIV's indices by the ones that are not in selectedIV
        print('stats index', selectedIV, 'passed down')
        print('stat index', notSelectedIV, 'randomized')

        print('Going into breeding, male IVs are', maleIVs)
        print('Going into breeding, female IVs are',femaleIVs)
        #print('Going into breeding, offspring IVs are',offspringIVs)
        print('-----------------------------------')
        for selected, val in enumerate(selectedIV):
            offspringIVs[val] = random.choice((maleIVs[val],femaleIVs[val]))
            if offspringIVs[val] == maleIVs[val]:
                print('Chosen from male IVs')
                
            else:
                print('Chosen from female IVs')
                
            
            print("Replaced stat", val+1, "with", offspringIVs[val])
            print('-----------------------------------')
        
        for notSelected, notVal in enumerate(notSelectedIV):
            offspringIVs[notVal] = random.randint(0, 31)
            print('Randomized number is', offspringIVs[notVal], "going into stat", notVal+1)

        #print('Going into breeding, male IVs are', maleIVs)
        #print('Going into breeding, female IVs are',femaleIVs)
        print('Resulting offspring IVs are',offspringIVs)
        

    #    # replace lists
    #    if perfectIVCount(offspringIVs) == perfectIVCount(maleIVs) and perfectIVCount(offspringIVs) == perfectIVCount(femaleIVs):
    #        for thirtyoneCount, thirtyone in enumerate(offspringIVs):
    #            if maleIVs[thirtyoneCount] != 0 and femaleIVs[thirtyoneCount] != 0:
    #                break
    #            elif offspringIVs[thirtyoneCount] > maleIVs[thirtyoneCount] and offspringIVs[thirtyoneCount] > femaleIVs[thirtyoneCount]:
    #                lowerNum = min(maleIVs[thirtyoneCount], femaleIVs[thirtyoneCount])
    #                if lowerNum == maleIVs[thirtyoneCount]:
    #                    maleIVs = offspringIVs
    #                    print("Replaced male pokemon")
    #                else:
    #                    femaleIVs = offspringIVs
    #                    print("Replaced female pokemon")


        if perfectIVCount(offspringIVs) > perfectIVCount(maleIVs):
            maleIVs = offspringIVs # these are lists
            print("Replaced male pokemon")

        elif perfectIVCount(offspringIVs) > perfectIVCount(femaleIVs):
            femaleIVs = offspringIVs
            print("Replaced female pokemon")

        print("Resulting Eggs are: ")
        print('Male: ', maleIVs, ' and has', perfectIVCount(maleIVs), '31s')
        print('Female: ', femaleIVs, ' and has', perfectIVCount(femaleIVs), '31s')
        print('-----------------------------------')

        eggCount += 1
        break

#print("Congrats! The child pokemon has max IV! It took ", eggCount-1,"number of eggs")
#print(maleIVs)
#print(femaleIVs)
#print(offspringIVs)
   



"""
        # if the 31 counts are the same, then choose the list with the lower value of index to replace
        if perfCount(childPerfCount, ivList3) == perfCount(parent2PerfCount, ivList2) and perfCount(parent1PerfCount, ivList1):
            for i in range(len(ivList3)):
                if ivList1[i] != 0 and ivList2[i] != 0:
                    break
                elif ivList3[i] > ivList2[i] or ivList3[i] > ivList1[i]:
                    lowerNum = min(ivList1[i], ivList2[i])
                    if lowerNum == ivList1[i]:
                        ivList1 = ivList3.copy()
                        print("Replaced male pokemon")
                        break
                    else:
                        ivList2 = ivList3.copy()
                        print("Replaced female pokemon")
                        break
            
"""

"""

for stat in startMaleStats.keys():
    if stat == 'Gender':
        continue
    while True:
        maleIV = input(f"Please input {stat} IV for male pokemon > ")

        if maleIV == 'perfect':
            startMaleStats[stat] = 31
            break
        elif maleIV in ['no good', 'decent', 'pretty good', 'very good', 'fantastic']:
            startMaleStats[stat] = 0
            break
        else:
            print("Invalid input. Please enter a valid IV")

for stat in startFemaleStats.keys():
    if stat == 'Gender':
        continue
    while True:
        femaleIV = input(f"Please input {stat} IV for female pokemon > ")

        if femaleIV == 'perfect':
            startFemaleStats[stat] = 31
            break
        elif femaleIV in ['no good', 'decent', 'pretty good', 'very good', 'fantastic']:
            startFemaleStats[stat] = 0
            break
        else:
            print("Invalid input. Please enter a valid IV")



destinyKnot = False

while destinyKnot == False:
    DK = input("Do you have destiny knot? [y/n] ")
    if DK == "y":
        destinyKnot = True

    elif DK == "n":
        destinyKnot = True
    else:
        print("Please input a correct input")


for iv in offspringStats.keys():
    if iv != 'Gender':
        while iv != 31:
  
            selectedIV = np.sort(random.sample(range(6), 3 if DK == "n" else 5))
            notSelectedIV = np.sort(list(set(range(6)) - set(selectedIV)))

            for i in selectedIV:
                key = random.choice(list(startMaleStats.keys(), startFemaleStats.keys()))

            break

        break
       
print(selectedIV)
print(offspringStats.values())


"""



















"""
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
    def __init__(self, ivList, gender): # assign each element in the list/array as an attribute for the class
        self.HP, self.ATK, self.DEF, self.SPA, self.SPD, self.SPE = ivList
        self.gender = gender







ivList1 = stats1.tolist() #pokemon 1
ivList2 = stats2.tolist() #pokemon 2
#ivList1 = []
#ivList2 = []
ivList3 = [0, 0, 0, 0, 0, 0] #initialize pokemon
perfectList = [31, 31, 31, 31, 31, 31] # perfect IV list to check with

counter =  1 # just counter things
parent1PerfCount = 0 # parent 1's perfect IV count
parent2PerfCount = 0 # parent 2's perfect IV count
childPerfCount  = 0 # child's perfect IV count

pokemon1 = [f"Please input {stat} IV for male pokemon > " for stat in ["HP","ATK","DEF","SPA","SPD","SPE"]] # formatted string which if you put in {} will replace whats in the list into there
pokemon2 = [f"Please input {stat} IV for female pokemon > " for stat in ["HP","ATK","DEF","SPA","SPD","SPE"]]

pokeGender = random.randint(0, 1)

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
#inputFunc(ivList1, pokemon1)
#inputFunc(ivList2, pokemon2)

# check if either of the iv lists matches max IV
#for testRuns in range(2): # will use later
#    print(counter)
    print("Going into breeding, male's stats are", ivList1)
    print("Going into breeding, female's stats are", ivList2)
while ivList1 != perfectList and ivList2 != perfectList:
    
    if perfCount(parent1PerfCount, ivList1) < 4 and perfCount(parent2PerfCount, ivList2) < 4: #I want to test if it's faster with 'and' or 'or'
        DK = False
    else:
        DK = True

    # choose 3 random numbers between 1 and 6 (but elements 0 to 5)
    selectedIV = np.sort(random.sample(range(6), 3 if DK == "n" else 5)) # 3 if default, 5 with destiny knot
    notSelectedIV = np.sort(list(set(range(6)) - set(selectedIV))) # this gets the list of notSelectedIV's indices by the ones that are not in selectedIV
#    print(notSelectedIV)

    # this replaces values in ivList3 with a random choice from each index of ivList1 and ivList2 depending on the indices of selectedIV
    for j, val in enumerate(selectedIV):
        ivList3[val] = random.choice((ivList1[val],ivList2[val]))
        #if ivList3[val] == ivList1[val]:
        #    print("---------------------")
        #    print("Chosen from list 1")
        #else:
        #    print("---------------------")
        #    print("Chosen from list 2")
        #print("Replaced stat", val+1, "with", ivList3[val])

    #print("Going into breeding, pokemon 1's stats are", ivList1)
    #print("Going into breeding, pokemon 2's stats are", ivList2)

    # this replaces the value that was not replaced with a random integer between 0 and 31
    for k, notVal in enumerate(notSelectedIV):
        ivList3[notVal] = random.randint(0, 31)
        #print(ivList3[notVal])
        print("Randomized number is", ivList3[notVal]," going into stat", notVal+1)
        #print("Going into breeding, pokemon 1's stats are", ivList1)
        #print("Going into breeding, pokemon 2's stats are", ivList2)

    #print("First pokemon's stats are ", ivList1)
    #print("Second pokemon's stats are ", ivList2)
    #print("The child pokemon's stats are ", ivList3)

    if ivList3 == perfectList:
        break

    else:
        ###### MAKE IT SO THAT THE CHILD COUNT OF 31'S WILL REPLACE THAT OF PARENTS ####
        perfCount(parent1PerfCount, ivList1)
        perfCount(parent2PerfCount, ivList2)
        perfCount(childPerfCount, ivList3)

        maleGender = "Male"
        femaleGender = "Female"

        maleStats = pokemon(ivList1, maleGender)
        femaleStats = pokemon(ivList2, femaleGender)

        # generate gender for offspring
        offspringGender = random.randint(0, 1)
        offspringStats = pokemon(ivList3, offspringGender)
 
        if offspringGender == 1:
            offspringStats.gender = "Male"
        else:
            offspringStats.gender = "Female"

        # if the 31 counts are the same, then choose the list with the lower value of index to replace
        if perfCount(childPerfCount, ivList3) == perfCount(parent2PerfCount, ivList2) and perfCount(parent1PerfCount, ivList1):
            for i in range(len(ivList3)):
                if ivList1[i] != 0 and ivList2[i] != 0:
                    break
                elif ivList3[i] > ivList2[i] or ivList3[i] > ivList1[i]:
                    lowerNum = min(ivList1[i], ivList2[i])
                    if lowerNum == ivList1[i]:
                        ivList1 = ivList3.copy()
                        print("Replaced male pokemon")
                        break
                    else:
                        ivList2 = ivList3.copy()
                        print("Replaced female pokemon")
                        break
            

        # if the child 31s are bigger than a parent's, then replace 
        if perfCount(childPerfCount, ivList3) > perfCount(parent1PerfCount, ivList1):
            ivList1 = ivList3  # create a copy instead of replacing or else it'll equal to each other before even initializing
            print("Replaced male's stats")

        if perfCount(childPerfCount, ivList3) > perfCount(parent2PerfCount, ivList2):
            ivList2 = ivList3 # create a copy instead of replacing or else it'll equal to each other before even initializing
            print("Replaced female's stats")


        print("New Stats")
        print("Male's stats", ivList1)
        print("Female's stats", ivList2)
        print("--------------------------------------------------")

        counter += 1
        break


print("Congrats! The child pokemon has max IV! It took ", counter-1,"number of eggs")
print(ivList3)
print(offspringStats.gender)
"""