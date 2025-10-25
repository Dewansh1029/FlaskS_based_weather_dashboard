📋 Features

Fetches real-time weather data for Bangalore.

Displays information in a clean format:

Weather in Bangalore: Humidity: 65%, Condition: Clear sky


Saves the output in a structured JSON file (weather_data.json).

Automatically reads your API key from a configuration file (config.ini).

🛠️ Requirements

Python 3.x

OpenWeather API key

Required packages:

pip install requests

⚙️ Setup Instructions

Clone the repository

git clone https://https://github.com/Dewansh1029/FlaskS_based_weather_dashboard
cd bangalore-weather-fetcher


Create and configure config.ini
In the same directory, create a file named config.ini with the following content:

[openweathermap]
api = YOUR_API_KEY_HERE


🔑 Replace YOUR_API_KEY_HERE with your actual OpenWeather API key.
You can get a free API key from https://openweathermap.org/api
.

Run the script

python app.py


Output Example

Weather in Bangalore: Humidity: 70%, Condition: Broken clouds
Weather data saved to weather_data.json

📁 Example Output (weather_data.json)
{
    "city": "Bangalore",
    "humidity": "70%",
    "condition": "Broken clouds"
}
