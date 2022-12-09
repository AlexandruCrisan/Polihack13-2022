import geopy.distance
from flask import Blueprint, request

from adapter.home_adapter import HomeAdapter
from database_ops.db_homes import DB_HOMES
from model.home import Home

urlHomes = Blueprint('views', __name__)

homes_table = DB_HOMES()

@urlHomes.route('/homes/<string:home_id>', methods=['POST'])
def addHome(home_id: str):
  home_json = request.json

  home_obj = Home(home_id, {"lat": float(home_json["lat"]), "lng": float(home_json["lng"])}, home_json["max_residents"], home_json["owner_username"])
  return homes_table.add_home(HomeAdapter.toJSON(home_obj))

@urlHomes.route('/homes/<string:home_id>', methods=['GET'])
def getHome(home_id: str):
  return homes_table.get_home(home_id)

@urlHomes.route('/homes/<string:home_id>', methods=['DELETE'])
def deleteHome(home_id: str):
  return homes_table.delete_home(home_id)

@urlHomes.route('/homes/distance/<string:home_id>', methods=['GET'])
def getDistanceToHome(home_id: str):
  lat = request.args.get("lat")
  lng = request.args.get("lng")

  home_json = homes_table.get_home(home_id)

  c1 = (float(lat), float(lng))
  c2 = (float(home_json["location"]["lat"]), float(home_json["location"]["lng"]))

  distance = geopy.distance.geodesic(c1, c2).km 
  return {"distance": distance}

