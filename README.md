# P.S: THE HOSTED SITE IS DOWN AS IT WAS VERY INEFFICIENT AND MESSY!

# Weather App 

This is a simple Flask application that displays weather information for a given city. It uses the OpenWeatherMap API to fetch weather data and the Photon geocoding API to obtain the location and timezone information for the city. The application is deployed on Render.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Firangi0799/Flask-Weather.git
   ```

2. Install the required dependencies:

   ```
   pip install flask geopy timezonefinder requests pytz
   ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org) by signing up for an account.

4. Replace the placeholder `API_KEY` in the `api` variable with your actual API key in the `app.py` file:

   ```python
   api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YOUR_API_KEY"
   ```

## Usage

1. Run the Flask application:

   ```
   python app.py
   ```

2. Open your web browser and go to [Weather-App](https://weather-app-1-3acz.onrender.com/) to access the application.

3. Enter the name of a city in the input field and click the "Get Weather" button.

4. The application will display the current weather condition, description, temperature, humidity, pressure, wind speed, and the current local time of the entered city.

## Deployment

The application is deployed on [Render](https://render.com). You can access the live version of the application at [https://your-app-name.onrender.com](https://weather-app-1-3acz.onrender.com/).

## Contributing

Contributions are welcome! If you find any issues or would like to add new features, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
