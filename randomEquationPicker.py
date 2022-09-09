# Read a file containing balanced equations
# Example: 2KOH+CO2=K2CO3+H2O
# Chosen JSON file format for input file
# JSON format for broader compatibility with industry, tools & tech
# Dictionary being a native construct of Python can be easily parsed

import json
import random

def getRandomEquation():
# eqn = json.loads("equationSource.json"); the "loads" method returned an error; ignored this option
# print(json.dumps(eqn), indent=4)



# Opens file and reads line by line into a dictionary
# open() method opens file in READ mode
# "eqn" is the file object
# "data" is the dictionary
# https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/
    with open("eqnSource.json") as eqn:
        data = json.load(eqn)
#        print(data)


# Convert dictionary of equations stored in object named "data" into a list of equations
# Then pick one (1) equation object out of the "equationList" object with the generated random number as the index

        equationList = list(data["Equations"])
        listLength = len(equationList)
        print(str(listLength))

# Generate a random number and use that random number to pick up a random equation from the list
        n = random.randint(0,(listLength-1))
        print(n)
        print(equationList[n])

    #    print(3*"\n")

        randEquation=""
        testEquation=""
        eqnDict={}
        lhsEqnDict={}
        rhsEqnDict={}
        

# Parse LHS of that randomly picked equation
# The randomly picked equation is still a dictionary containing LHS and RHS objects
# LHS and RHS objects are also dictionaries
# Each LHS object contains multiple tuples
# Get the length of the LHS dictionary and iterate through the list of tuples

        j = len(equationList[n]["LHS"])
        # print(j)
        lhsIndex = 0

        lhsPairs = equationList[n]["LHS"]
        for key, value in lhsPairs.items():
            print(key, value)

            eqnDict[key] = value
            lhsEqnDict[key] = value
            randEquation = randEquation + str(value) + str(key)
            testEquation = testEquation + "__" + str(key)
            
            if lhsIndex < j-1:
                randEquation = randEquation + "+"
                testEquation = testEquation + "+"

            lhsIndex += 1
            
        

 # Once LHS is done concatenate "=" sign before concatenating RHS to the equation
        randEquation = randEquation + "="
        testEquation = testEquation + "="
    #    print(randEquation)

    # Parse RHS of that randomly picked equation
        k = len(equationList[n]["RHS"])
        # print(k)
        rhsIndex = 0
       
        rhsPairs = equationList[n]["RHS"]
        for key, value in rhsPairs.items():
            print(key, value)
            eqnDict[key] = value
            rhsEqnDict[key] = value
            randEquation = randEquation + str(value) + str(key)
            testEquation = testEquation + "__" + str(key)

            if rhsIndex < k-1:
                randEquation = randEquation + "+"
                testEquation = testEquation + "+"

            rhsIndex += 1
                
            

        print(randEquation)
        print("*******")
        print(testEquation)
        print("////////")
        print(eqnDict)
        
    #    eqnDict = json.loads(eqnString)
    #    print(eqnDict)


        return({"origEquation":randEquation, "tstEquation":testEquation, "equationDict":eqnDict, "lhsEquationDict":lhsEqnDict, "rhsEquationDict":rhsEqnDict})

# Test call

# Uncomment the below line ONLY to test this file by itself
# Otherwise calling from the compareEqn.py file will make this execute twice
# getRandomEquation()