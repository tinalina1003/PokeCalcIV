"""Method using randint"""

from numpy import *
import random
import time






# Random number with system time
worstIV = 0

maxIV = 31

count = 0

#IV = random.randint(worstIV, maxIV)

HPIV = input("What is your HP IV > ")

if HPIV == "perfect":
    print ("You already have perfect IV")

elif HPIV == "no good" or HPIV == "decent" or HPIV == "pretty good" or HPIV == "very good" or HPIV == "fantastic":

    while HPIV == "no good" or HPIV == "decent" or HPIV == "pretty good" or HPIV == "very good" or HPIV == "fantastic":

        HPIV = random.randint(worstIV, maxIV)

        if HPIV < 31:
            #print ("Current HP IV is", HPIV)
            HPIV = "no good"
            count += 1
        else:
            print ("You got max IV after", count ,"tries!")
            print ("Current HP IV is", HPIV)


"""
if HP == "no good":
    HP = random.randint(worstIV, maxIV)
    if HP < 15:       
        print (HP)
        print("Low roll sorry")
    else:
        print (HP)
        print ("High IV")
 
else:
    HP = "test"
    print (HP)

"""



#IV = random.randint(worstIV, maxIV)
"""
while int(IV) < 31:
    IV = random.randint(worstIV, maxIV)
    print (int(IV))
    count += 1

print ("It took", count, "amount of tries to get Perfect")
"""
"""
def randIV():

    if int(IV) == 0:
        print ("Your new IV is No Good")
        int(IV) == "No Good"

    elif int(IV) > 0 and int(IV) <= 15:
        print ("Your new IV is Decent")
        int(IV) == "Decent"

    elif int(IV) >= 16 and int(IV) <= 25:
        print ("Your new IV is Pretty Good")
        int(IV) == "Pretty Good"

    elif int(IV) >= 26 and int(IV) < 30:
        print ("Your new IV is Very Good")
        int(IV) == "Very Good"

    elif int(IV) == 30:
        print ("Your new IV is Fantastic")
        int(IV) == "Fantastic"

    elif int (IV) == 31:
        print("Your new IV is Perfect")
        int(IV) == "Perfect, no need to reroll"

 
def randIVnum(value):

    if value != "perfect":
        randIV()
    
    else:
        print("Your stat is perfect. No need to reroll")



def randIV():

    if HP == 0:
        print ("Your new IV is No Good")
        HP  == "No Good"

    elif HP  > 0 and HP  <= 15:
        print ("Your new IV is Decent")
        HP  == "Decent"

    elif HP  >= 16 and HP  <= 25:
        print ("Your new IV is Pretty Good")
        HP  == "Pretty Good"

    elif HP  >= 26 and HP  < 30:
        print ("Your new IV is Very Good")
        HP  == "Very Good"

    elif HP  == 30:
        print ("Your new IV is Fantastic")
        HP  == "Fantastic"

    elif HP  == 31:
        print("Your new IV is Perfect")
        HP  == "Perfect"

HP = (input("What IV is your HP? > "))

randIVnum(HP)
randIVnum(Def)

print (int(IV))
print ("Your HP IV is", HP)

while (HP != "Perfect"):

    print (HP)
    HP = int(IV)
    
"""



