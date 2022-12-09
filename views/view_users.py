from flask import Blueprint, request

from adaptor.refugee_adaptor import RefugeeAdaptor
from database_ops.db_users import DB_USERS
from model.provider import Provider
from model.refugee import Refugee

urlUser = Blueprint('views', __name__)

users_table = DB_USERS()
ref_adaptor = RefugeeAdaptor()

@urlUser.route('/users/test', methods=['GET'])
def test():
  return "MERGE BINE"
@urlUser.route('/users/provider/<string:id>', methods=['POST'])
def postProvider(id: str):
  user_json = request.json

  provider_entity = Provider(id, user_json["name"], user_json["phone_number"], user_json["email"])
  return users_table.addUser(ref_adaptor.toJson(provider_entity) )

@urlUser.route('/users/provider/<string:id>', methods=['GET'])
def getProvider(id: str):
  return users_table.get_user(id)

@urlUser.route('/users/refugee/<string:id>', methods=['POST'])
def postRefugee(id: str):
  user_json = request.json

  refugee_entity = Refugee(id, user_json["name"], user_json["phone_number"], user_json["nationality"], user_json["location"], user_json["skills"])
  return users_table.addUser(RefugeeAdaptor.toJSON(refugee_entity) )

@urlUser.route('/users/refugee/<string:id>', methods=['GET'])
def getRefugee(id: str):
  return users_table.get_user(id)