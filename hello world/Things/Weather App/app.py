from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # This allows cross-origin requests for your frontend

API_KEY = '339f7554a54f57b436f6e081455c9037' # Replace with your own API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name is required!"}), 400

    # Make a request to the OpenWeatherMap API
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)
