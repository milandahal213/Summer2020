# Import necessary library
import time
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Create a global string variable named val
val='0'

# Create a function to change the value of a variable
def changeValue():
    global val
    val=int(val)
    val+=1
    if val>9:
        val=0 
    return str(val)

# Create a link so that a client can access the value 
# Open a new tab on your browser and enter IP:/getvalue to see the latest value
# You can do a GET call to the url 'IP:/getvalue' to access the latest value 
@app.route('/getvalue', methods=['GET'])
def getvalue():
    val=changeValue()
    try:
        return str(val)
    except Exception as e:
        return str(e)

# Add favicon link to avoid 404 error
@app.route('/favicon.ico', methods=['GET'])
def favicon():
    a='ignore'
    return a

# Start the Flask server on port 5000 
# Add use_reloader=False to make it work on Jupyter Notebook
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded = True, use_reloader=False)