import database_ops.setup as setup


class DB_HOMES():

    def __init__(self):
        self.__homeTable = setup.startSetup("test-homes")

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
        response = self.__homeTable.put_item(
            Item=homeObjJSON
        )
        return response

    def delete_home(self, id: str):
        response = self.__homeTable.delete_item(
        Key = {
            'id': id
        }
        )
        return response
    
    def get_all_homes(self):
        response = self.__homeTable.scan(AttributesToGet=['id', 'location', 'max_residents'])
        return response["Items"]