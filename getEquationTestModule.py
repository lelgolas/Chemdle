# Import the module to get the original equation
# https://csatlas.com/python-import-file-module/#import_a_file_in_the_same_directory
import getOriginalEquation

#origEquation = "2H2+O2=2H2O"
# Example: 2KOH+CO2=K2CO3+H2O
#print(origEquation)

origEquation = getOriginalEquation.getOriginalEquation()
print(origEquation)