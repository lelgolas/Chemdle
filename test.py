import json

eqnString = "{\"1\":'C2H6O',\"3\":'O2',\"2\":'CO2',\"3\":'H2O'}"
print(eqnString)
eqnDict = json.loads(str(eqnString))
print(eqnDict)