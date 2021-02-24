from flask import Flask
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
import requests
import os



KEY = os.getenv("GOOGLE_API_KEY")

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def getTest() :
    return 'in GET route'

@app.route('/post', methods=['POST'])
def postTest():
    return 'in POST route'

@app.route('/map')
def pizza():
    response = requests.get(f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.977753,-93.2650108&radius=32000&type=restaurant&keyword=pizza&key={KEY}')
    return response.json()
  