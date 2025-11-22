def parse_intent(text: str):
    t = text.lower()
    ask_weather = any(w in t for w in ["temperature", "weather", "rain"])
    ask_places = any(p in t for p in ["places", "visit", "attractions", "go"])
    return {"ask_weather": ask_weather or not ask_places, "ask_places": ask_places or not ask_weather}