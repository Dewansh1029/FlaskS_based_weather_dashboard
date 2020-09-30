import requests
import configparser
from  flask import Flask ,render_template, request

# uique identifier for the flask session 
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods=['POST','GET'])
def render_results():
    city_name=request.form['cityname']
    state_name=request.form['statename']
    country_code=request.form['countrycode']
    
    api_key=get_api_key()
    data=get_weather_results(city_name,state_name,country_code,api_key)
    temp ="{0:.2f}".format(data["main"]["temp"])
    feels_like =data["main"]["feels_like"]
    weather = data["weather"][0]["main"]
    location = data["name"]
    description= data["weather"][0]["description"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    return render_template('results.html',location=location,temp=temp,feels_like=feels_like,weather=weather,description=description,temp_min=temp_min,temp_max=temp_max)

def get_api_key():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(city_name,state_code,country_code, api_key):
    api_url="http://api.openweathermap.org/data/2.5/weather?q={},{},{}&appid={}".format(city_name,state_code,country_code,api_key)
    #api_url  ="http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperical&appid={}".format(zip_code , api_key)
    r = requests.get(api_url)
    return r.json()
    
if __name__== '__main__':
    app.run()
