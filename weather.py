import os
import time

import requests
from pypresence import Presence

def main():
    API_KEY = ""  # get a key at https://www.weatherbit.io/account/create
    CLIENT_ID = ""
    # Parameters below at https://www.weatherbit.io/api
    CITY_NAME = ""
    COUNTRY = ""
    LANG = ""
    url = "https://api.weatherbit.io/v2.0/current?city={}&country={}&lang={}&key={}".format(CITY_NAME, COUNTRY, LANG, API_KEY)

    discord_rpc = Presence(CLIENT_ID)
    discord_rpc.connect()
    print("Rich presence connected!")

    while True:
        response = requests.get(url).json()
        data = response['data'][0]

        temperature = int(data['temp'])
        wind_speed = int((data['wind_spd'])*3.6) # m/s to km/h formula
        wind_cdir_full = data['wind_cdir_full']
        weather_icon = data['weather']['icon']
        weather_desc = data['weather']['description']
        details = f"{temperature}°C, {wind_speed} km/h {wind_cdir_full}"
        print(details, weather_icon)

        discord_rpc.update(details=weather_desc, state=details, large_image=weather_icon, small_image=weather_icon)
        time.sleep(300) # 5 minutes


if __name__ == '__main__':
    main()
