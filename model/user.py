class User():
    def __init__(self, id: str, name: str, phone_number: str):
        self.__id = id
        self.__name = name
        self.__phone_number = phone_number

    def get_id(self):
      return self.__id

    def get_name(self):
      return self.__name

    def get_phone_number(self):
      return self.__phone_number