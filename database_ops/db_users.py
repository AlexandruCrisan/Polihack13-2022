import database_ops.setup as setup


class DB_USERS():

    def __init__(self):
        self.__userTable = setup.startSetup("test-users")

    def get_user(self, username):
        response = self.__userTable.get_item(
            Key={
                'username': username
            }
        )
        try:
            return response["Item"]
        except KeyError:
            return {"ErrorMessage": "User Does not Exist"}

    def addUser(self, userObjJSON):  # + Check existance
        response = self.__userTable.put_item(
            Item=userObjJSON
        )
        return response

    def getAllUsers(self):
        response = self.__userTable.scan(AttributesToGet=['id', 'name', 'profile_picture', 'profile_picture_extension', 'role'])
        sorted(response, key=lambda x:x[1])
        return response
