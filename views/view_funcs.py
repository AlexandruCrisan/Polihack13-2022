import os

import geopy.distance
from dotenv import load_dotenv
from flask import Blueprint, request
from googleplaces import GooglePlaces, types

from database_ops.db_homes import DB_HOMES

urlFuncs = Blueprint('views', __name__)

load_dotenv()

API_KEY = os.getenv('MAPS_API_KEY')

google_places = GooglePlaces(API_KEY)

homes_table = DB_HOMES()

def respects_filters(home, filters):
  try:
    home_JSON = homes_table.get_home(home["id"])
    if filters["max_residents"] < home_JSON["max_residents"]:
      return False
  except Exception:
    return True

  return True



########################################################## Nearby Hospitals
@urlFuncs.route('/nearby_hospitals', methods=['GET'])
def getHospitals():
  lat = request.args.get("lat")
  lng = request.args.get("lng")
  radius = int(request.args.get("radius"))

  query_result = google_places.nearby_search(
        # lat_lng ={'lat': 46.1667, 'lng': -1.15},
        lat_lng ={'lat': lat, 'lng': lng},
        radius = radius,
        types =[types.TYPE_HOSPITAL])

  response = []
  for place in query_result.places:
    response.append( {"name": place.name, "coords":{"lat":float(place.geo_location['lat']), "lng": float(place.geo_location['lng'])}} )
  return response

########################################################## Nearby Homes

@urlFuncs.route('/nearby_homes', methods=['GET'])
def getHomes():
  lat = request.args.get("lat")
  lng = request.args.get("lng")
  radius = int(request.args.get("radius"))

  min_residents = request.args.get("min_residents")

  all_homes = homes_table.get_all_homes()
  response = []
  for home in all_homes:
    print(home)
    c1 = (float(lat), float(lng))
    c2 = (float(home["location"]["lat"]), float(home["location"]["lng"]))

    distance = geopy.distance.geodesic(c1, c2).km 
    print(f"{home['id']} -> {distance}")
    if distance <= radius and int(min_residents) <= int(home["max_residents"]):
      response.append(home)

  return response

  

  