from flask import Flask, request, jsonify, Response
import random, json

app = Flask(__name__)

@app.route("/savelist")
#POST

def savelist():
    

#write json to a file

@app.route("/getlist")
#GET

#read json from a file


###########
#deploy on pythonanywhere.com
# 1) get local storage going in the new structure
# 2) write the endpoints to save and get
# 3) update your javascript to use fetch to save and 

app.run(debug=True, port=5001)