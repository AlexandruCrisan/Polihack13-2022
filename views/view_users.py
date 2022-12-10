from flask import Blueprint, request

from adapter.provider_adapter import ProviderAdapter
from adapter.refugee_adapter import RefugeeAdapter
from database_ops.db_users import DB_USERS
from model.provider import Provider
from model.refugee import Refugee

urlUser = Blueprint('views', __name__)

users_table = DB_USERS()

dons = {
  "money": 0,
  "food": 0,
  "clothes": 0
}

@urlUser.route('/users/test', methods=['GET'])
def test():
  return "MERGE BINE"

########################################################## General

@urlUser.route('/login', methods=['GET'])
def loginUser():
  username = request.args.get("username")
  password = request.args.get("password")
  userJSON = users_table.get_user(username)

  try:
    if userJSON["password"] != password:
      return ("Incorrect Password", 403)
  except Exception:
    return ("Incorrect Username", 403)
  return (users_table.get_user(username), 200)

@urlUser.route('/users/<string:username>', methods=['GET'])
def getUser(username: str):
  return users_table.get_user(username)

########################################################## Provider

@urlUser.route('/users/provider/<string:username>', methods=['POST'])
def postProvider(username: str):
  user_json = request.json

  provider_entity = Provider(username, user_json["password"], user_json["name"], user_json["phone_number"], user_json["email"], [], [])
  return users_table.addUser(ProviderAdapter.toJSON(provider_entity))

########################################################## Refugee

@urlUser.route('/users/refugee/<string:username>', methods=['POST'])
def postRefugee(username: str):
  user_json = request.json

  refugee_entity = Refugee(username, user_json["password"], user_json["name"], user_json["phone_number"], user_json["nationality"], user_json["location"], user_json["skills"], dons)
  return users_table.addUser(RefugeeAdapter.toJSON(refugee_entity) )

