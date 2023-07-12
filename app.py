from flask import Flask, render_template, request
import requests
import pytz
from geopy.geocoders import Photon
from timezonefinder import TimezoneFinder
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    city = request.args.get("city")
    if not city:
        return render_template("index.html")

    # Get the location of the city
    geolocator = Photon(user_agent="geoapiExercises")
    location = geolocator.geocode(city)

    # Get the timezone of the city
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    # Get the current time in the city
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")

    # Get the weather for the city
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=fe952f9b69a7b12dd4e42d3f2a55f6f4"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']

    return render_template("index.html", city=city, current_time=current_time, condition=condition, description=description, temp=temp, humidity=humidity, pressure=pressure, wind=wind)

if __name__ == "__main__":
    app.run(debug=True)
