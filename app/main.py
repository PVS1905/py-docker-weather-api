import os
import requests
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

def get_weather() -> None:

    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={SECRET_KEY}&q=Paris&aqi=no")
    print(response.json())


if __name__ == "__main__":
    get_weather()
