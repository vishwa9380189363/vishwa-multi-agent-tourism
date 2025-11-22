from fastapi import FastAPI, Query
from typing import Optional
from app.agents.geocode import geocode_place
from app.agents.weather import weather_current
from app.agents.places import places_suggest

app = FastAPI(title="Multi-Agent Tourism System")

@app.get("/weather")
def get_weather(place: str = Query(..., description="Place name")):
    loc = geocode(place)
    if not loc:
        return {"message": "I don’t know if this place exists."}
    w = weather_current(loc["lat"], loc["lon"])
    return {"place": loc["display_name"], "weather": w}

@app.get("/places")
def get_places(place: str = Query(..., description="Place name"), limit: int = 5):
    # Call the correct geocode function
    loc = geocode_place(place)
    if not loc:
        return {"message": f"I don’t know if the place '{place}' exists."}
    
    # Use the lat/lon from geocode_place
    p = places_suggest(loc["lat"], loc["lon"], limit=limit)
    return {"place": loc["display_name"], "places": p


@app.get("/plan")
def plan(place: str, ask_weather: bool = True, ask_places: bool = True, limit: int = 5):
    loc = geocode(place)
    if not loc:
        return {"message": "I don’t know if this place exists."}
    result = {"place": loc["display_name"]}
    if ask_weather:
        result["weather"] = weather_current(loc["lat"], loc["lon"])
    if ask_places:
        result["places"] = places_suggest(loc["lat"], loc["lon"], limit=limit)
    return result