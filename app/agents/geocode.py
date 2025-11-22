import requests

def geocode_place(place: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "multi-agent-tourism-app/1.0 (your_email@example.com)"  
        # Replace with your email or project name
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"Place '{place}' not found")
    return data[0]