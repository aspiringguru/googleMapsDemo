import googlemaps
from datetime import datetime
from config import *

print("API_KEY:", API_KEY)

gmaps = googlemaps.Client(key=API_KEY)


# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Taringa, QLD",
                                     "Kenmore, QLD",
                                     mode="transit",
                                     departure_time=now)
print("\n\n transit - directions_result:", directions_result)

directions_result = gmaps.directions("Taringa, QLD",
                                     "Kenmore, QLD",
                                     mode="walking",
                                     departure_time=now)
print("\n\n walking - directions_result:", directions_result)

directions_result = gmaps.directions("Taringa, QLD",
                                     "Kenmore, QLD",
                                     mode="bicycling",
                                     departure_time=now)
print("\n\n bicycling - directions_result:", directions_result)

directions_result = gmaps.directions("Taringa, QLD",
                                     "Kenmore, QLD",
                                     mode="driving",
                                     departure_time=now)
print("\n\n driving - directions_result:", directions_result)

'''
possible modes
driving
walking
bicycling
transit
'''
len(directions_result)
list(directions_result[0].keys())

['bounds', 'copyrights', 'legs', 'overview_polyline', 'summary', 'warnings', 'waypoint_order']

directions_result[0]['bounds']
directions_result[0]['copyrights']
directions_result[0]['legs']
len(directions_result[0]['legs'])

list(directions_result[0]['legs'][0].keys())
['distance', 'duration', 'duration_in_traffic', 'end_address', 'end_location', 'start_address', 'start_location', 'steps', 'traffic_speed_entry', 'via_waypoint']

directions_result[0]['legs'][0]['duration_in_traffic']
directions_result[0]['legs'][0]['distance']
directions_result[0]['legs'][0]['duration']

len(directions_result[0]['legs'][0]['steps'])

totDistance = 0
totDuration = 0
numSteps = len(directions_result[0]['legs'][0]['steps'])
for i in range(numSteps):
    print("i:", i)
    #print (directions_result[0]['legs'][0]['steps'][i])
    print (directions_result[0]['legs'][0]['steps'][i]['distance'])
    totDistance += directions_result[0]['legs'][0]['steps'][i]['distance']['value']
    print (directions_result[0]['legs'][0]['steps'][i]['duration'])
    totDuration += directions_result[0]['legs'][0]['steps'][i]['duration']['value']

print("totDistance:", totDistance)
print("totDuration:", totDuration)
