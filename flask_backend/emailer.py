import requests
import travel
import explore
import model
import json

from multiprocessing import Pool

attractions_json = None
breakfast_json = None
lunch_json = None
dinner_json = None
flights_json = None

def generate_email(destination, start_location):
    global attractions_json, flights_json, breakfast_json, lunch_json, dinner_json
    attractions_json = explore.explore_attractions(destination).json()
    breakfast_json = explore.get_businesses(destination, "breakfast").json()
    lunch_json = explore.get_businesses(destination, "lunch").json()
    dinner_json = explore.get_businesses(destination, "dinner").json()
    flights_json = find_cheapest_flight(start_location, destination)

def pop_attraction():
    if (attractions_json != None):
        return attractions_json['response']['groups'][0]['items'].pop()
    else:
        return None

def pop_breakfast():
    if (breakfast_json != None):
        return breakfast_json['businesses'].pop()
    else:
        return None

def pop_lunch():
    if (lunch_json != None):
        return lunch_json['businesses'].pop()
    else:
        return None

def pop_dinner():
    if (dinner_json != None):
        return dinner_json['businesses'].pop()
    else:
        return None

def get_flight(number):
    if (flights_json != None):
        return flights_json[number]
    else:
        return None

def find_cheapest_flight(start_location, destination):
    start_airport_json = travel.find_closest_airports(start_location)
    destination_airport_json = travel.find_closest_airports(destination)
    
    start_airport = start_airport_json.json()["results"][0]["name"]
    destination_airport = destination_airport_json.json()["results"][0]["name"]
    best_flights_json = travel.find_best_airplanes(start_airport, destination_airport)
    return best_flights_json