from model.user import User


class Provider(User):
    def __init__(self, username: str, password: str, name: str, phone_number: str, email: str):
        super().__init__(username, password, name, phone_number)
        self.__email = email
    
    def get_email(self):
      return self.__email