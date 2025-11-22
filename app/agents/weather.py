import requests

def weather_current(lat: float, lon: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "precipitation_probability"
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    j = r.json()
    temp = j.get("current_weather", {}).get("temperature")
    hourly = j.get("hourly", {})
    prob_list = hourly.get("precipitation_probability")
    prob = prob_list[0] if isinstance(prob_list, list) and prob_list else None
    return {"temperature_c": temp, "rain_probability_percent": prob}