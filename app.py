from flask import Flask
import requests
app = Flask(__name__)

@app.route('/get', methods=['GET'])
def getTest() :
    return 'in GET route'

@app.route('/post', methods=['POST'])
def postTest():
    return 'in POST route'

@app.route('/map')
def pizza():
    response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.977753,-93.2650108&radius=32000&type=restaurant&keyword=pizza&key=AIzaSyBsf7l3iI39TwWrf6YbrBZzvNx2YD3662s')
    return response.text
  