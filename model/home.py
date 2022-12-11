
import json
import os
from urllib.request import urlopen

from geopy.geocoders import Nominatim

MAPS_API_KEY = os.getenv("MAPS_API_KEY")

class Home:
  def __init__(self, id: str, location: dict, max_residents: int, owner_username: str, new: int):
    self.__id = id
    self.__location = location
    self.__max_residents = max_residents
    self.__owner_username = owner_username
    self.__new = new
    geolocator = Nominatim(user_agent="geoapiExercises")
    address = geolocator.reverse(str(self.__location["lat"])+", "+ str(self.__location["lng"]))
    address = address.raw["address"]
    self.__street_name = f"{address.get('road', '')} {address.get('house_number')}, {address.get('city')}"

    url = f"https://maps.googleapis.com/maps/api/streetview/metadata?size=400x400&location={str(self.__location['lat'])},{str(self.__location['lng'])}&key={MAPS_API_KEY}"
    response = urlopen(url)
    data_json = json.loads(response.read())

    self.__location_image = f"https://maps.googleapis.com/maps/api/streetview?pano={data_json['pano_id']}&size=600x400&key={MAPS_API_KEY}"
    
    # print(address)

  def get_id(self):
    return self.__id

  def get_new(self):
    return self.__new

  def get_location(self):
    return self.__location

  def get_max_residents(self):
    return self.__max_residents

  def get_owner_username(self):
    return self.__owner_username

  def get_street_name(self):
    return self.__street_name

  def get_location_image(self):
    return self.__location_image
    