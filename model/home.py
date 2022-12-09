class Home:
  def __init__(self, id: str, location: dict, max_residents: int, owner_username: str):
    self.__id = id
    self.__location = location
    self.__max_residents = max_residents
    self.__owner_username = owner_username

  def get_id(self):
    return self.__id

  def get_location(self):
    return self.__location

  def get_max_residents(self):
    return self.__max_residents

  def get_owner_username(self):
    return self.__owner_username
    