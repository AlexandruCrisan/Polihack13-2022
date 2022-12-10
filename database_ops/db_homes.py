import database_ops.setup as setup
from database_ops.db_users import DB_USERS


class DB_HOMES():

    def __init__(self):
        self.__homeTable = setup.startSetup("test-homes")
        self.__dbUsers = DB_USERS()

    def get_home(self, id):
        response = self.__homeTable.get_item(
            Key={
                'id': id
            }
        )
        try:
            return response["Item"]
        except KeyError:
            return {"ErrorMessage": "Home Does not Exist"}

    def add_home(self, homeObjJSON):
        self.__homeTable.put_item(
            Item=homeObjJSON
        )

        # Add them into the provider's account
        userJSON = self.__dbUsers.get_user(homeObjJSON["owner_username"])
        houses = userJSON["houses"]

        houses.append(homeObjJSON["id"])
        return self.__dbUsers.updateHouses(homeObjJSON["owner_username"], houses)


    def delete_home(self, id: str):
        response = self.__homeTable.delete_item(
        Key = {
            'id': id
        }
        )
        return response
    
    def get_all_homes(self):
        response = self.__homeTable.scan(AttributesToGet=['id', 'location', 'max_residents', 'street_name'])
        return response["Items"]