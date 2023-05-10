import random

worstIV = 0

maxIV = 31

count = 0


IV = input("choose a number > ")

#IV = random.randint(worstIV, maxIV)

while int(IV) < 31:
    IV = random.randint(worstIV, maxIV)
    print (int(IV))
    count += 1

print ("It took", count, "amount of tries to get Perfect")



