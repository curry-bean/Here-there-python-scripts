import os
import requests
from plyer import notification
from datetime import datetime
from enum import Enum


# These variables are used in API url
# You need to have OpenWeather API Key
# You can register and receive a key from https://openweathermap.org/
WEATHER_API_KEY = '5440c834fe04793d192f43e12e18a42b'

CITY = os.getenv("CITY")

class TimeSlot(Enum):
    MORNING = "\U0001F305"
    EVENING = "\U0001F319"

class Weather(Enum):
    SUNNY = "\U0001F31E"
    CLOUD = "\U00002601"
    HEAVY_RAINY = "\U000026C8"
    CLOUD_RAINY = "\U0001F327"
    CLOUD_SNOW = "\U0001F328"
    LIGHTHING = "\U0001F329"
    FOGGY = "\U0001F32B"
    SNOW = "\U00002744"
    MOON_FACE = "\U0001F31B"
    THERMOMETER = "\U0001F321"
    

def get_current_time_slot(sunrise, sunset, timezone):
    """
    :param sunrise: sunrise time in UNIX(Epoch) time
    :type int

    :param sunset: sunset time in UNIX(Epoch) time
    :type int

    :param timezone: users timezone in UNIX(Epoch) time
    :type int

    :return: Emoji string wrt time slot 
    """
    now = datetime.now().strftime("%H:%M")
    sunrise = datetime.fromtimestamp(sunrise).strftime("%A, %B %d, %Y %H:%M:%S")
    sunset = datetime.fromtimestamp(sunset).strftime("%A, %B %d, %Y %H:%M:%S")

    sunrise_utc = sunrise.split(" ")[-1].split(":")[:2]
    sunset_utc = sunset.split(" ")[-1].split(":")[:2]

    # Morning 
    if int(now.split(":")[0]) >= int(sunrise_utc[0]) and int(now.split(":")[0]) < int(sunset_utc[0]):
        return TimeSlot.MORNING.value
    # Evening
    elif int(now.split(":")[0]) < int(sunrise_utc[0]) or int(now.split(":")[0]) >= int(sunset_utc[0]):
        return TimeSlot.EVENING.value
    else:
        return TimeSlot.EVENING.value
    

def get_weather_emoji(weather_id):
    """
    Finds the suitable emoji for given weather situation
    :param weather_id: id of the weather status
    :type int
    :return: Emoji string wrt weather status
    """
    
    if weather_id < 300:
        return Weather.LIGHTHING.value
    elif weather_id < 400:
        return Weather.CLOUD_RAINY.value
    elif weather_id < 600:
        return Weather.HEAVY_RAINY.value
    elif weather_id < 700:
        return Weather.SNOW.value
    elif weather_id < 800:
        return Weather.FOGGY.value
    elif weather_id == 800:
        return Weather.SUNNY.value
    elif weather_id < 900:
        return Weather.CLOUD.value
    return Weather.SUNNY.value

def send_notification(weather_emoji, time_slot_emoji, weather_description, tempature):
    """
    Send notification with given information
    
    :param weather_emoji: current weather's status emoji string
    :type Weather(enum)

    :param time_slot: suitable emoji string wrt current time's slot.
    :type TimeSlot(enum)

    :param weather_description: current weather description
    :type string

    :param tempature: degree of the weather in celsius
    :type string

    :return: Nothing
    """

    now = datetime.now().strftime("%H:%M")
    city = "City: " + CITY + "\n"
    time = "Time: " + now + time_slot_emoji + "\n"
    description = "Description: " + weather_description + "  " + weather_emoji + "\n"
    temp = "Tempature: " + tempature + "°C " + Weather.THERMOMETER.value
    message = city + time + description + temp 
    toaster = ToastNotifier()
    toaster.show_toast("Weather Forecast", message,
                   icon_path=None,
                   duration=10,
                   threaded=True)

def parse_json(data):
    """
    Parses the data and retrives the necessary information

    :param data: json file which is fetched
    :type dict

    :return: Nothing
    """

    weather = data["weather"][0]["description"]
    weather_id = int(data["weather"][0]["id"])
    tempature = str(data["main"]["temp"])
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]
    timezone = data["timezone"]

    time_slot = get_current_time_slot(sunrise, sunset, timezone)
    emoji = get_weather_emoji(weather_id)
    send_notification(emoji, time_slot, weather, tempature)


def main():
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "&APPID=" + WEATHER_API_KEY + "&units=metric"
    res = requests.get(url)
    data = res.json()
    parse_json(data)


main()