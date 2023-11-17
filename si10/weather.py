from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import numpy as np
import pandas as pd


def json_to_dataframe(json_data):
    # Crear un diccionario con los datos relevantes
    data = {
        "Temperature": np.array([json_data["main"]["temp"]]),
        "Feels Like": np.array([json_data["main"]["feels_like"]]),
        "Min Temperature": np.array([json_data["main"]["temp_min"]]),
        "Max Temperature": np.array([json_data["main"]["temp_max"]]),
        "Pressure": np.array([json_data["main"]["pressure"]]),
        "Humidity": np.array([json_data["main"]["humidity"]]),
        "Wind Speed": np.array([json_data["wind"]["speed"]]),
        "Wind Direction": np.array([json_data["wind"]["deg"]]),
        "Cloud Coverage": np.array([json_data["clouds"]["all"]]),
        "Visibility": np.array([json_data["visibility"]]),
    }

    # Crear un DataFrame de pandas
    df = pd.DataFrame(data)

    return df.to_html()
    
load_dotenv()


def get_current_weather(city="Kansas City"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)
    

    print("\n")
    pprint(weather_data)