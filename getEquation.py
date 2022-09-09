import compareEqn
from flask import Flask

app = Flask(__name__)

@app.route("/getEquation", methods=['GET', 'POST'])
def testEquation():
    return(compareEqn.compareEquation())
    

#    return "Hello, World!"

#if __name__ == '__main__':
#    app.run(port=1881, debug=True)