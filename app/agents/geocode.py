import requests

def geocode_place(place: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }
    headers = {
        # Must be a valid identifier with contact info
        "User-Agent": "multi-agent-tourism-app/1.0 (contact: rachapallivishwa9363@gmail.com)"
    }
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"Place '{place}' not found")
    return data[0]