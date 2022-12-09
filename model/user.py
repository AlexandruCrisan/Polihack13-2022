class User():
    def __init__(self, username: str, password: str, name: str, phone_number: str):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__phone_number = phone_number

    def get_username(self):
      return self.__username

    def get_password(self):
      return self.__password

    def get_name(self):
      return self.__name

    def get_phone_number(self):
      return self.__phone_number