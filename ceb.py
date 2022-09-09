from hmac import new
from itertools import count
import json
import randomEquationPicker
import compareEqn
from flask import Flask, request

origEquationDict={}

app = Flask(__name__)

@app.route("/", methods=['GET'])
def getEquation():
#    getEquation = randomEquationPicker.getRandomEquation()
#    originalEquation = getEquation["origEquation"]
#    tstEquation = getEquation["tstEquation"]
#    equationDict = getEquation["equationDict"]
    
    # eqnTable = ""
    newTestEquation = getTestEquation()

#    for key, value in equationDict.items():
#        print(key + "!!!" + str(value))
#        newTestEquation = newTestEquation + "<input type='text' name='"+key+"'/>"+key
        

    print(newTestEquation)
    with open('ceb.html', 'r') as f:
        # cebPage = f.read().format(tstEqn=json.dumps(equationDict))
        cebPage = f.read().format(newTstEqn=json.dumps(newTestEquation))
    # Have to figure out why eqnTable that is declared as a string needs to be treated as a dictionary in the format call
    #    cebPage = f.read().format(eqnTbl=json.dumps(eqnTable))
    
    return(cebPage)

@app.route("/compEquation", methods=['GET', 'POST'])
def compEquation():
    global origEquationDict

    form_data = request.form
    # print(form_data)

    frmDataPairs = form_data.items()

    cebResult = ""
    errorCount = 0

#  Compare dictionaries - To Do:  May 18, 2022.  DONE - May 24, 2022

    for key, value in frmDataPairs:
        print(key, value)
        
        origValue = origEquationDict.get(key)        
        formValue = form_data.get(key)
        print("BEFORE COMPARISON " + key + ":")
        print("Original Value: " + str(origValue) + ", Form Value: " + formValue)
        try:
            if (int(formValue) != int(origValue)):
                errorCount += 1
                cebResult = cebResult + "Value you entered for " + key + " is: " + "<p style='color:red'>" + str(formValue) + "</p>"
                print("---------------")
                print("AFTER COMPARISON" + key + ":")
                print("Original Value: " + str(origValue) + ", Form Value: " + formValue)
            else:
                cebResult = cebResult + "Value you entered for " + key + " is: " + "<p style='color:green'>" + str(formValue) + "</p>"
        except ValueError:
            cebResult = "Sorry! Please enter a valid natural number"

    print("Original Equation Dict in compEquation:")
    for key, value in origEquationDict.items():
        print(key, value)
    
    if errorCount == 0:
        cebResult = "<p style='color:green'>That's Correct!!! </p>" + cebResult
    else:
        cebResult = "Sorry!  Please try again <br>" + cebResult

    with open('ceb_result.html', 'r') as f:
        # cebResultPage = f.read().format(cebRslt=json.dumps(cebResult))
        cebResultPage = f.read().format(cebRslt=json.dumps(cebResult))
    
    return(cebResultPage)


def getTestEquation():
    getEquation = randomEquationPicker.getRandomEquation()
    equationDict = getEquation["equationDict"]
    lhsEqnDict = getEquation["lhsEquationDict"]
    rhsEqnDict = getEquation["rhsEquationDict"]

    global origEquationDict
    origEquationDict = equationDict

    print("Original Equation Dict in getTestEquation:")
    print(origEquationDict)
    
    # newTestEquation = ""
    tstEquationString = ""

    #for key, value in equationDict.items():
    #    print(key + "!!!" + str(value))
    #    newTestEquation = newTestEquation + "<input type='text' name='"+key+"'/>"+key
    
    for key, value in lhsEqnDict.items():
        tstEquationString = tstEquationString + "<input type='text' name='"+key+"'/>"+key
    
    tstEquationString = tstEquationString + "  ------->  "
    for key, value in rhsEqnDict.items():
        tstEquationString = tstEquationString + "<input type='text' name='"+key+"'/>"+key

    print(tstEquationString)

    return(tstEquationString)
        

if __name__ == '__main__':
    app.run(port=1881, debug=True, threaded=True)