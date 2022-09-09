# Import the module to get the original equation
# https://csatlas.com/python-import-file-module/#import_a_file_in_the_same_directory
# Uncomment the last line to call the function to run the module independently

import randomEquationPicker

#origEquation = "2H2+O2=2H2O"
# Example: 2KOH+CO2=K2CO3+H2O
#print(origEquation)

def compareEquation():

    # getEquation = randomEquationPicker.getRandomEquation()
    # originalEquation = getEquation["origEquation"]


    yourAnswer = input("Enter the coefficients to balance the equation:")
    print(yourAnswer)

    if (yourAnswer == "originalEquation"):
        return("That's correct!")
    else:
        return("That's incorrect. Please try again")

# Uncomment the following line to run this module independently
#compareEquation()