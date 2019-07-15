import googlemaps
from datetime import datetime
from config import *

print("API_KEY:", API_KEY)

gmaps = googlemaps.Client(key=API_KEY)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print("geocode_result:", geocode_result)

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print("reverse_geocode_result:", reverse_geocode_result)


# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Queen St Mall",
                                     "Kenmore, QLD",
                                     mode="transit",
                                     departure_time=now)

print("directions_result:", directions_result)
