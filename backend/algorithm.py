from .models import Weather


def get_weather(city, date):
    return Weather(city, date, 10, 20)