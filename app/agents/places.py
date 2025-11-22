import requests

def places_suggest(lat: float, lon: float, limit: int = 5, radius_m: int = 8000):
    overpass_url = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json][timeout:25];
    (
      node(around:{radius_m},{lat},{lon})["tourism"];
      way(around:{radius_m},{lat},{lon})["tourism"];
      relation(around:{radius_m},{lat},{lon})["tourism"];
    );
    out center;
    """
    r = requests.post(overpass_url, data=query, timeout=30)
    r.raise_for_status()
    data = r.json().get("elements", [])
    names = []
    for el in data:
        tags = el.get("tags", {})
        name = tags.get("name")
        if name and name not in names:
            names.append(name)
        if len(names) >= limit:
            break
    return names