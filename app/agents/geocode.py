import requests
import os

USER_AGENT = os.getenv("USER_AGENT", "MultiAgentTourism/1.0 (contact@example.com)")

def geocode(place: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place, "format": "json", "limit": 1}
    r = requests.get(url, params=params, headers={"User-Agent": USER_AGENT}, timeout=10)
    r.raise_for_status()
    data = r.json()
    if not data:
        return None
    item = data[0]
    return {"lat": float(item["lat"]), "lon": float(item["lon"]), "display_name": item.get("display_name", place)}