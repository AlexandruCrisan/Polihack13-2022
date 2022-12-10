import database_ops.setup as setup
from database_ops.db_users import DB_USERS


class DB_CASH_BANK():
  def __init__(self):
    self.__cashTable = setup.startSetup("test-bank")
    self.__dbUsers = DB_USERS()

  def get_bank_value(self):
    response = self.__cashTable.get_item(
      Key={
            'id': "total"
          }
    )
    try:
      return response["Item"]
    except KeyError:
      return {"ErrorMessage": "Bank Does not Exist"}

  def add_funds(self, funds: int):
    total = self.get_bank_value()
    
    total["value"] = int(total["value"]) + funds

    response = self.__cashTable.put_item(
      Item=total
    )
    return response

  def extract_funds(self, username: str, funds_requested: int):
    total = self.get_bank_value()

    if total == 0:
      return 

    # Extract funds from the bank
    funds_received = int(total["value"]) if (int(funds_requested) > int(total["value"])) else int(funds_requested)

    total["value"] = int(total["value"]) - funds_received

    self.__cashTable.put_item(Item=total)

    # Add them into the refugee's account
    userJSON = self.__dbUsers.get_user(username)
    dons = userJSON["donations"]

    dons["money"] = int(dons["money"]) + int(funds_received)

    return self.__dbUsers.updateDonations(username, dons)
   