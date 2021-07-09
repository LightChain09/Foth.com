import requests
import json


def weather_processor(request):
    api_key = "935774a3-98ed-40db-91f8-659affb755ba"
    response = requests.get(f"http://api.airvisual.com/v2/nearest_city?key={api_key}")
    json_response = json.loads(response.text)

    city = json_response["data"]["city"]
    state = json_response["data"]["state"]
    country = json_response["data"]["country"]
    temperature = json_response["data"]["current"]["weather"]["tp"]
    humidity = json_response["data"]["current"]["weather"]["hu"]
    icon = json_response["data"]["current"]["weather"]["ic"]

    return {
        "city": city,
        "state": state,
        "country": country,
        "temperature": temperature,
        "humidity": humidity,
        "icon": icon,
    }